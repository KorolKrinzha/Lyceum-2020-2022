import sys
import os
import re
import string
from nltk import word_tokenize
from nltk.probability import FreqDist
import nltk
import pymorphy2
from nltk.corpus import stopwords


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
 

new2=[]
with open(work_file,'r') as myself:
    for word in words (myself):
        
        
        p = morph.parse(word)[0]
        if p.normal_form not in rus:
            new2.append (p.normal_form)




    

    

text = ""

for i in range (len(new2)):
    if len(new2[i])>2:
        text+=new2[i]+" "
    





text = text.lower()
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("-", "")
text = text.replace("_", "")
text = text.replace("?", "")
text = text.replace("[", "")
text = text.replace("]", "")
text = text.replace("'", "")
text = text.replace(";", "")
text = text.replace("'", "")
text = text.replace(":", "")
text = text.replace("'", "")
text = text.replace(")", "")
text = text.replace("(", "")
text = text.replace("он", "")
text = text.replace("\bи\b", "")
text = text.replace("ну", "")

text = text.replace(u"\u2018", "")
text = text.replace(u"\u2019", "")


text_tokens = word_tokenize(text)

text = nltk.Text(text_tokens)

fdist = FreqDist(text)

print (fdist.most_common(20))


