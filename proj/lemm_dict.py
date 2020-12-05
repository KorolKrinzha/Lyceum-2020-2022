

import sys
import os
import re
import string
from nltk import word_tokenize
from nltk.probability import FreqDist
import nltk
import pymorphy2
from nltk.corpus import stopwords

import matplotlib.pyplot as plt



morph = pymorphy2.MorphAnalyzer()



def words(stringIterable):
    
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word


rus = []
with open('stopit.txt','r') as myself:
    for word in words (myself):
        
        rus.append (word)






work_file = 'voyna-i-mir-tom-1.txt'
 
text = ""
with open(work_file,'r') as myself:
    for word in words (myself):
        
        
        p = morph.parse(word)[0]
        if p.normal_form not in rus and p.tag.POS == 'NOUN':
            text+=p.normal_form+" "




    

    




text_tokens = word_tokenize(text)

text = nltk.Text(text_tokens)

fdist = FreqDist(text)


print (fdist.most_common(20))
fdist.plot(20,cumulative=False)


