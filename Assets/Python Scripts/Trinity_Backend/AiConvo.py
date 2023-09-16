'''
prompt = "in this location, based on this {memory} of the tow people, and their {personality}, 
give a short and meaningful ocnversation between the two people. 
Format the person's name as key, and what they say as value."

convo = langchian output
convo = extractConvo(output)

convo_summary = summarize()
summarize()

summarize(): json = if person == "bob", summary_gpt(),  summarize new info for each person and store in their seperate memory


data structure - 

{0:   name: bob,
      personality: , 
      memory: 
        1: ,
        2:   
1:  name: alice,
    personality: , 
    memory: 
        0: ,
        2:   
2:  name: Cat,
    personality: , 
    memory: 
        0: ,
        1: , 
}

'''
import json
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.chains import LLMChain


with open('env.json', 'r') as json_file:
    env_dict = json.load(json_file)
openai_api = env_dict["OPEN_AI_API"]

# chat_model = ChatOpenAI(openai_api_key=openai_api)
chat_model = ChatOpenAI()

talkPrompt = PromptTemplate.from_template("{name1} and {name2} are meeting at {location}. {name1} is {personality1}, and {name2} is {personality2}. From {name1s} previous interactions with {name2}, {name1} thinks the following about {name2}: {oneThinkTwo}. From {name2}'s previous interactions with {name1}, {name2} thinks the following about {name1}: {twoThinkOne}. Please simulate a short but meaningful conversation between the two people as lines of a dialogue script.")

summarizePrompt = PromptTemplate.from_template("{name1} and {name2} are meeting at {location}. {name1} is {personality1}, and {name2} is {personality2}. From {name1's} previous interactions with {name2}, {name1} thinks the following about {name2}: {oneThinkTwo}. From {name2}'s previous interactions with {name1}, {name2} thinks the following about {name1}: {twoThinkOne}. The conversation they just had was the following: {conversation}, and in response {name1} did this: {name1action} while {name2} did this: {name2action}. Please provide a full summary of the interactions, incorporating previous interaction information as well as the most recent one into a single summary, and factor in {name1}'s personality traits as influencing the summary.")


def getTalkPrompt(id1: int, id2: int, location: str, data: dict) -> PromptTemplate:
    name1 = data[id1]["name"]
    name2 = data[id2]["name"]
    personality1 = data[id1]["personality"]
    personality2 = data[id2]["personality"]

    oneThinkTwo = data[id1]["interactions"][id2]
    twoThinkOne = data[id2]["interactions"][id1]

    return talkPrompt.format(name1=name1, 
                            name2=name2,location=location, 
                            personality1=personality1, 
                            personality2 = personality2,
                            oneThinkTwo = oneThinkTwo,
                            twoThinkOne = twoThinkOne
                            )
                            
with open("/Trinity_Backend/history/silicon_valley_ex.json","r") as f:
    data = json.load(f)

print(getTalkPrompt(0,1,"the park", data))
# def getSummarizePrompt(id1: int, id2: int, location: str, people_storage: str) -> PromptTemplate

name_schema = ResponseSchema(name = "name", description="The name of the person")
message_schema = ResponseSchema(name = "message", description="What the person says")
response_schemas = [
    name_schema,
    message_schema
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

chain = LLMChain(llm=chat_model, 
                   prompt=talkPrompt,
                   output_parser=output_parser)


response = chain.run()


def chainRun(ch)
response_as_dict = output_parser.parse(response.content)

