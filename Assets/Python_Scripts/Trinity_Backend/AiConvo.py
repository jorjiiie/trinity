import json
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.chains import LLMChain
import nltk
import numpy as np
import os
from nltk.sentiment import SentimentIntensityAnalyzer

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "env.json")
with open(path, 'r') as json_file:
    env_dict = json.load(json_file)
openai_api = env_dict["OPEN_AI_API"]

chat_model = ChatOpenAI(openai_api_key=openai_api)

class AiConvo():
    def __init__(self):
        self.data = {}
        self.talkPrompt = PromptTemplate.from_template("""You are the chief screen writer for the show Silicon Valley, and you are writing the next scene between the two characters. A scene is usually 4-6 round of conversation with new information and good dynamic between the characters.
                                          {name1} is {personality1}, and {name2} is {personality2}. 
                                          From {name1}'s previous interactions with {name2}, {name1} thinks the following about {name2}: {oneThinkTwo}. 
                                          From {name2}'s previous interactions with {name1}, {name2} thinks the following about {name1}: {twoThinkOne}. 
                                          Format the person's name as key, and what they say as value, output should be a dictionary.""")
        self.script = {}

    def getTalkPrompt(self, id1: str, id2: str, data: dict) -> PromptTemplate:
        name1 = data[id1]["first_name"]
        name2 = data[id2]["first_name"]
        personality1 = data[id1]["personality"]
        personality2 = data[id2]["personality"]

        oneThinkTwo = data[id1]["interactions"][id2]
        twoThinkOne = data[id2]["interactions"][id1]

        return self.talkPrompt.format(name1=name1,
                                name2=name2,
                                personality1=personality1, 
                                personality2 = personality2,
                                oneThinkTwo = oneThinkTwo,
                                twoThinkOne = twoThinkOne
                                )

    def get_script(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, "history/silicon_valley_ex.json")
        with open(path,"r") as f:
            self.script = json.load(f)        
        with open(os.path.join(dirname,"information/reactions.json"),"r") as f:
            self.reactions_json = json.load(f)    
        self.reactions_list = [item for item in self.reactions_json["key"].keys()]
        self.reactions_values = [self.reactions_json["score"][item] for item in self.reactions_list]


    def get_convo(self, id1:str, id2:str) -> str:
        # chat_model = ChatOpenAI()
        self.get_script()
        input_prompt = self.getTalkPrompt(id1,id2, self.script)
        response = chat_model.predict(text=input_prompt)        
        return response

    
    def get_action(self,):
        pass

    def get_convo_and_action(self, characters: str):
        #sample input:"1 2"
        id1, id2 = characters.split(" ")
        convo = self.get_convo(id1, id2)
        action1, action2 = self.get_react(convo, id1, id2)
        convo_and_action = "Conversation^" + convo + "/nAction%1^" + action1 + "/nAction%2^" + action2
        return convo_and_action
    

    def get_react(self, conversation: str, id1: str, id2: str) -> (str, str):
        """Given a conversation and two people's ids, calculate their reactions"""

        def normal_distribution(x , mean , sd):
            prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
            return prob_density

        ids = [id1, id2]

        actions = []
        for i in range(2):
            personality_probabilities = [self.script[ids[i]]["reactions"][item] for item in self.reactions_list]

            sia = SentimentIntensityAnalyzer()
            score = sia.polarity_scores(conversation)['compound']
            print(score)

            PDF = normal_distribution(np.array(self.reactions_values), score, 0.2)
            PDF = [PDF[i] * personality_probabilities[i] for i in range(len(PDF))]
            
            # normalize the pdf LOL
            PDF = PDF / np.sum(PDF)

            # can just replace the i for i ... with just the list of reactions LOL

            x = np.random.choice(self.reactions_list,size=1, p = PDF)

            actions.append(x)

        return (actions[0][0], actions[1][0])



AiConvo = AiConvo()
print(AiConvo.get_convo_and_action("1 2"))


# summarizePrompt = PromptTemplate.from_template("{name1} and {name2} are meeting at {location}. {name1} is {personality1}, and {name2} is {personality2}. From {name1}'s previous interactions with {name2}, {name1} thinks the following about {name2}: {oneThinkTwo}. From {name2}'s previous interactions with {name1}, {name2} thinks the following about {name1}: {twoThinkOne}. The conversation they just had was the following: {conversation}, and in response {name1} did this: {name1action} while {name2} did this: {name2action}. Please provide a full summary of the interactions, incorporating previous interaction information as well as the most recent one into a single summary, and factor in {name1}'s personality traits as influencing the summary.")






# name_schema = ResponseSchema(name = "name", description="The name of the person")
# message_schema = ResponseSchema(name = "message", description="What the person says")
# response_schemas = [
#     name_schema,
#     message_schema
# ]
# output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# chain = LLMChain(llm=chat_model, 
#                    prompt=talkPrompt,
#                    output_parser=output_parser)


# response = chain.run()
# response_as_dict = output_parser.parse(response.content)

