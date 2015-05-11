# Feature extraction codes for twitter
The list of features to use is : 
1) Unigram features : Extract the most relevant words from each of the categories
2) Prior polarity sum from a dictionary of word polarity (WordNet...), score of Hashtag words * 2 
3) Count POS tags in a tweet (adj, NN , Verb)
4) Emoticons scores , from a dictionary 
5) Length of a tweet
6) time of the day : value between 0 and 23 for hours in the day
7) Presence of exclamation, counts of exclamation marks
8) Presence of negation
9) Presence of (?), counts of question marks
10) Frequence of capitalized letters in the tweet
11) add more if needed ...

This repository contains codes to map tweets to feature vectors
