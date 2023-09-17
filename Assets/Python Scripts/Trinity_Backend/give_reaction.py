import nltk
import numpy as np
import json
from nltk.sentiment import SentimentIntensityAnalyzer

with open("information/reactions.json","r") as f:
    reactions_json = json.load(f)

reactions_list = [item for item in reactions_json.keys()]

def react(conversation: str, id1: str, id2: str) -> (str, str):
    """"""Given a conversation and two people's ids, calculate their reactions"""

    def normal_distribution(x , mean , sd):
        prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
        return prob_density

    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(conversation)['compound']

    
    print(score)

    personality_values = {}
    PDF = normal_distribution([personality_values[action] for action in  ], score, 0.2)

    # normalize the pdf LOL
    PDF = PDF / np.sum(PDF)

    # can just replace the i for i ... with just the list of reactions LOL

    x = np.random.choice(reactions_list,size=1, p = PDF)

    # figure out what reactions go where and are associated with what

    
    



react("hows your day! it's pretty good i am having fun", "a", "b")
    



    
    
    
