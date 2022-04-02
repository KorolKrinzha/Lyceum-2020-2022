# -*- coding: utf-8 -*- 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer


original_text_name = 'To_Kill_a_Mockingbird.txt'
result_text_name = "Results.txt"






with open(original_text_name, 'r') as file:
    text = file.read().replace('\n', '')
    
sizestopwords = len(text)
tokens = word_tokenize(text)
tokens_sent = sent_tokenize(text, language="english")
#print (text)

print (tokens_sent)


print (tokens)






download_stopwords = stopwords.words('english') 

stop_text = []
for i in tokens:
    if i not in download_stopwords:
        stop_text.append(i)

sizenostopwords =len(stop_text)


file = open(result_text_name,'w')
try:
        arr = stop_text
        for i in range (len(arr)):
            s = arr[i]
            file.write(s)
            file.write(' ')
        
finally:
        file.close()




print ("THE DIFFERENCE IS ", sizestopwords-sizenostopwords, "WORDS")
