import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer 






original_text_name = 'after_death_original.txt'
result_text_name = "Results.txt"

with open(original_text_name, 'r') as file:
    text = file.read().replace('\n', '')


download_stopwords = stopwords.words('russian') #стоп-слова

stop_text = []

tokens = word_tokenize(text) #разбиение на слова
for i in tokens:
    if i not in download_stopwords:
        stop_text.append(i)





stems = []
stemmer = SnowballStemmer("russian")    
for token in tokens:
    token = stemmer.stem(token)
    if token != "":
        stems.append(token)


print("stems:", stems)
