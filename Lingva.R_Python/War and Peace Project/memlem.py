import sys
import os
import re
import string
from nltk import word_tokenize
from nltk.probability import FreqDist
import nltk

from nltk.corpus import stopwords


def words(stringIterable):
    
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word


rus = []
with open('stopit.txt','r') as myself:
    for word in words (myself):
        
        rus.append (word)



#russian_stopwords = stopwords.words("russian")
#russian_stopwords.extend(['это', 'нею', 'было', 'на', 'князь', 'он', 'я', 'она', 'и', 'было'])
#print (russian_stopwords)


work_file = 'voyna-i-mir-tom-1.txt'
 

new2=[]
with open(work_file,'r') as myself:
    for word in words (myself):
        if word not in rus:
            new2.append (word)



    

text = ""

for i in range (len(new2)):
    text+=new2[i]+" "
    





text = text.lower()#один регистр

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
text = text.replace("''", "")
text = text.replace(":", "")
text = text.replace("``", "")

text_tokens = word_tokenize(text)

text = nltk.Text(text_tokens)

fdist = FreqDist(text)

print (fdist.most_common(10))


