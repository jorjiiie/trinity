'''
prompt = "in this location, based on this {memory} of the tow people, and their {personality}, 
give a short and meaningful ocnversation between the two people. follwing {person 1}, {person 2}."
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

with open('env.json', 'r') as json_file:
    env_dict = json.load(json_file)
openai_api = env_dict["OPEN_AI_API"]

chat_model = ChatOpenAI(openai_api_key=openai_api)

text = "What would be a good company name for a company that makes colorful socks?"


# print(chat_model.predict("hi!"))


# chat_model.predict("hi!")


talkPrompt = PromptTemplate.from_template("{name1} and {name2} are meeting at {location}. {name1} is {personality1}, and {name2} is {personality2}. From {name1's} previous interactions with {name2}, {name1} thinks the following about {name2}: {oneThinkTwo}. From {name2}'s previous interactions with {name1}, {name2} thinks the following about {name1}: {twoThinkOne}. Please simulate a short but meaningful conversation between the two people as lines of a dialogue script.")

summarizePrompt = PromptTemplate.from_template("{name1} and {name2} are meeting at {location}. {name1} is {personality1}, and {name2} is {personality2}. From {name1's} previous interactions with {name2}, {name1} thinks the following about {name2}: {oneThinkTwo}. From {name2}'s previous interactions with {name1}, {name2} thinks the following about {name1}: {twoThinkOne}. The conversation they just had was the following: {conversation}, and in response {name1} did this: {name1action} while {name2} did this: {name2action}. Please provide a full summary of the interactions, incorporating previous interaction information as well as the most recent one into a single summary.")


def readData(file_name: str):
    #read json file into dict
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return data

def getTalkPrompt(id1: int, id2: int, location: str, people_storage: json) -> PromptTemplate:
    data = readData(people_storage)
    name1 = data[id1]["name"]
    name2 = data[id2]["name"]
    personality1 = data[id1]["personality"]
    personality2 = data[id2]["personality"]

    oneThinkTwo = data[id1]["opinions"][id2]
    twoThinkOne = data[id2]["opinions"][id1]

    return talkPrompt.format(name1=name1, 
                            name2=name2,location=location, 
                            personality1=personality1, 
                            personality2 = personality2,
                            oneThinkTwo = oneThinkTwo,
                            twoThinkOne = twoThinkOne
                            )


print(getTalkPrompt(0,1,"the park", readData("silicon_valley_ex.json")))
# def getSummarizePrompt(id1: int, id2: int, location: str, people_storage: str) -> PromptTemplate:



chain = LLMChain(
    llm=ChatOpenAI(),
    prompt=chat_prompt,
    output_parser=CommaSeparatedListOutputParser()
)
chain.run("")
