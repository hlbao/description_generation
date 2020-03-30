import os
import re
import random
import math
from unidecode import unidecode
import numpy as np
from numpy.random import random_sample



def compute_perplexity(doc_word,doc_topic,topic_word):

    sum_ln_pt = 0
    sum_t = 0
    for doc_n,a in enumerate(doc_word): #each line represents a document
        wordlist = []
        for i, ele in enumerate(a):
            if ele != 0:
                wordlist.append(i)  # the id of words (in the document) is stored in wordlist
        sum_t += len(wordlist)       # total how many words
        pt = 0               #  sum of log probability of each document
        for t_id in wordlist:          # for each word
            pz=0
            for topic_n,tw in enumerate(topic_word):  #visit all topics
                p_tz= tw[t_id]                        #the t_id words in the topic_n topic
                p_zd= doc_topic[doc_n][topic_n]       #the topic_n^th topic in the doc_n^th document
                pz +=  p_tz*p_zd
            pt += math.log(pz)
        sum_ln_pt += pt
    perp = math.exp(-sum_ln_pt / sum_t)

    return perp
