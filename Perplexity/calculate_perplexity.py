# -*- coding: UTF-8-*-
import numpy
import math
import string
import matplotlib.pyplot as plt
import re

def dictionary_found(wordlist):               #for each word trained by model, we 
  #make it "word as key, probability as value" dictionary
    word_dictionary1={}
    for i in xrange(len(wordlist)):
        if i%2==0:
            if word_dictionary1.has_key(wordlist[i])==True:
                word_probability=word_dictionary1.get(wordlist[i])
                word_probability=float(word_probability)+float(wordlist[i+1])
                word_dictionary1.update({wordlist[i]:word_probability})
            else:
                word_dictionary1.update({wordlist[i]:wordlist[i+1]})
        else:
            pass
    return word_dictionary1

def look_into_dic(dictionary,testset):          #for each word in test set, find its probability in dictionary 
    #'''Calculates the TF-list for perplexity'''    
    frequency=[]
    letter_list=[]
    a=0.0
    for letter in testset.split():
        if letter not in letter_list:
            letter_list.append(letter)
            letter_frequency=(dictionary.get(letter))
            frequency.append(letter_frequency)
        else:
            pass
    for each in frequency:
        if each!=None:
            a+=float(each)
        else:
            pass
    return a


def f_testset_word_count(testset):                                     #count word number in test set
    #'''reture the sum of words in testset which is the denominator of the formula of Perplexity'''
    testset_clean=testset.split()
    return (len(testset_clean)-testset.count("\n"))

def f_perplexity(word_frequency,word_count):             #calculate preplexity 
    #'''Search the probability of each word in dictionary
   # Calculates the perplexity of the LDA model for every parameter T'''
    duishu=-math.log(word_frequency)
    kuohaoli=duishu/word_count
 
    perplexity=math.exp(kuohaoli)
    return perplexity

def graph_draw(topic,perplexity):             #graph draw for topic and preplexity
    x=topic
    y=perplexity
    plt.plot(x,y,color="red",linewidth=2)
    plt.xlabel("Number of Topic")
    plt.ylabel("Perplexity")
    plt.show()


topic=[]
perplexity_list=[]
f1=open('/users/pc/Desktop/description_generation/Perplexity/candidate.txt','r')      #test 
# f1=open('/users/pc/Desktop/description_generation/Perplexity/candidate2.txt','r')      #test 


testset=f1.read()
testset_word_count=50        
for i in xrange(50):
    dictionary={}
    topic.append(4*i)  #confused, but works, since i learned some other codes, this line aims to count topic                                                  
    trace="/users/pc/Desktop/description_generation/Perplexity/model-final-"+str(2*i)+".txt"   
    f=open(trace,'r')
    text=f.readlines()
    word_list=[]
    for line in text:
        if "Topic" not in line:
            line_clean=line.split()
            word_list.extend(line_clean)    
        else:
            pass
    word_dictionary=dictionary_found(word_list)
    frequency=look_into_dic(word_dictionary,testset)      
    perplexity=f_perplexity(frequency,testset_word_count)       
    perplexity_list.append(perplexity)        
graph_draw(topic,perplexity_list)



#https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0
