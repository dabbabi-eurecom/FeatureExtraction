# emoticon score extraction from a tweet 
# using an emoticon dictionary in resources/emoticon.txt
import re
# emoticons scores by category , change weighting if needed
emo_scores = {'Positive': 3, 'Extremely-Positive': 4, 'Negative':1,'Extremely-Negative': 0,'Neutral': 2}
emo_score_list={}
fi = open("../resources/emoticon.txt","r")
l=fi.readline()

while l:
    l=l.replace("\xc2\xa0"," ")
    li=l.split(" ")
#    print li[len(li)-1].split("\t")
#li=li[:-1].append(li[len(li)-1].split("\t"))
#   print li[:-1]
#    print li
    l2=li[:-1]
    l2.append(li[len(li)-1].split("\t")[0])
#l2.append(li[len(li)-1].split("\t")[1][:-1])
    sentiment=li[len(li)-1].split("\t")[1][:-1]
    score=emo_scores[sentiment]
    l2.append(score)
#    print l2
    for i in range(0,len(l2)-1):
        emo_score_list[l2[i]]=l2[len(l2)-1]
    l=fi.readline()
#print len(emo_score_list)
for i in emo_score_list.keys():
    print i+"   :   "+str(emo_score_list[i])



