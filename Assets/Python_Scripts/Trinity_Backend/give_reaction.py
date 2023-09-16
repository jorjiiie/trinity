import nltk
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer

def react(conversation: str, id1: str, id2: str) -> (str, str):
    """"Given a conversation and two people's ids, calculate their reactions"""

    def normal_distribution(x , mean , sd):
        prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
        return prob_density

    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(conversation)['compound']

    print(score)
    num = 5

    PDF = normal_distribution(0.8, score, 0.2)

    # normalize the pdf LOL
    PDF = PDF / np.sum(PDF)

    # can just replace the i for i ... with ju
    x = np.random.choice([i for i in range(num)],size=1, p = PDF)

    # figure out what reactions go where and are associated with what
    num_reactions  = 5 # set this in actual code

    
    



react("hows your day! it's pretty good i am having fun", "a", "b")
    



    
    
    
