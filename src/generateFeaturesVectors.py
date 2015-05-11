# this file contains elemantary functions to map a tweet into a vector
# e.g : emoticons score, POS tags counts ...

import re
# emoticons scores by category , change weighting if needed
def createEmoticonDictionary():
    emo_scores = {'Positive': 3, 'Extremely-Positive': 4, 'Negative':1,'Extremely-Negative': 0,'Neutral': 2}
    emo_score_list={}
    fi = open("../resources/emoticon.txt","r")
    l=fi.readline()

    while l:
        l=l.replace("\xc2\xa0"," ")
        li=l.split(" ")
        l2=li[:-1]
        l2.append(li[len(li)-1].split("\t")[0])
        sentiment=li[len(li)-1].split("\t")[1][:-1]
        score=emo_scores[sentiment]
        l2.append(score)
        for i in range(0,len(l2)-1):
            emo_score_list[l2[i]]=l2[len(l2)-1]
        l=fi.readline()
    return emo_score_list

def emoticonScore(tweet):
    "calculate the aggregate score of emoticons in a tweet"
    s=0;
    d=createEmoticonDictionary()
    l=tweet.split(" ")
    for i in range(0,len(l)):
        if l[i] in d.keys():
            print d[l[i]]
            s=s+d[l[i]]
    return s

#t=raw_input("tweet :")
#print emoticonScore(t)
