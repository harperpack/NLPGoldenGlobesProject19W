# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import nltk
import pdb
import re

#nltk.download('punkt')

count = 0
count_host = 0
host_list = ["tina", "fey", "Tina", "Fey", "Amy", "Poehler", "amy", "poehler"]
tweet_list = []
tweeted = []
words = []
stop_words = ['a','able','about','across','after','all','almost',\
                          'also','am','among','an','and','any','are','as',\
                          'at','be','because','been','but','by','can',\
                          'cannot','could','dear','did','do','does','either',\
                          'else','ever','every','for','from','get','got',\
                          'had','has','have','he','her','hers','him','his',\
                          'how','however','i','if','in','into','is','it',\
                          'its','just','least','let','like','likely','may',\
                          'me','might','most','must','my','neither','no',\
                          'nor','not','of','off','often','on','only','or',\
                          'other','our','own','rather','said','say','says',\
                          'she','should','since','so','some','than','that',\
                          'the','their','them','then','there','these','they',\
                          'this','tis','to','too','twas','us','wants','was',\
                          'we','were','what','when','where','which','while',\
                          'who','whom','why','will','with','would','yet',\
                          'you','your']
stop_words_globes = ['goldenglobes', 'golden', 'globe', 'globes', "'s", "n't"\
                     '...']
tot_stop_words = stop_words + stop_words_globes

def remove_punctuation_and_caps_and_stop_words(word_list):
    new_list = []
    for word in word_list:
        # NOT REMOVING # OR @
        new_word = re.sub(r'[,!?-_()$&*/"\:;.“”…]','',word)
        new_word = re.sub(r"'",'',new_word)
        new_word = new_word.lower()
        if new_word not in tot_stop_words:
            new_list.append(new_word)
    return new_list

word = ''
with open("gg2015.json", "r") as file:
    tweets = json.load(file)
    for line in tweets:
        #pdb.set_trace()
        count += 1
        tweet_list.append(line['text'])
        if count > 99999:
            break
#        for word in line['text']:
#            print(word)
#        if count > 5:
#            break
#print(count)
#for tweet in tweet_list:
#    print(tweet)
#    print("\n")
#    count_host += 1
#    if count_host > 5:
#        break

print(tweet_list[0])

#for tweet in tweet_list:
#    for i in range(len(tweet)):
#        if tweet[i] == ' ':
#            words.append(word)
#            word = ''
#        else:
#            word += tweet[i]
#        if i == len(tweet) - 1:
#            tweets.append(words)
#            words = []
#print(tweets[0:5])

#for i in range(len(tweet_list)):
#    for indx in range(len(tweet_list[i])):
#        if tweet_list[i][indx] == ' ' or tweet_list[i][indx] == ',' or tweet_list[i][indx] == '.':
#            words.append(word)
#            word = ''
#        else:
#            word += tweet_list[i][indx]
#        if indx == len(tweet_list[i]) - 1:
#            tweeted.append(words)
#            words = []

big_long_tweet = ''
for twet in tweet_list:
    #token = nltk.word_tokenize(twet)
    #tweeted.append(token)
    big_long_tweet += twet
    big_long_tweet += ' '
big_token = nltk.word_tokenize(big_long_tweet)
#ind_freq = nltk.FreqDist(tweeted)
clean_token = remove_punctuation_and_caps_and_stop_words(big_token)
tot_freq = nltk.FreqDist(clean_token)
print(tot_freq.most_common(50))
