import csv
from nltk.tokenize import word_tokenize
import re
from fuzzywuzzy import fuzz

with open('greedy.csv', newline='\n', encoding='utf8') as File:
    reader = csv.reader(File)
    for row in reader:
        
        for sentence in list(row[i] for i in [1]):
            tokens = word_tokenize(sentence)
            result = re.findall(r'(соленый огурец|солёный огурец|Соленый огурец|Солёный огурец)', sentence)

            if len(result)>0:

                res = fuzz.ratio(sentence, 'Соленый огурец на полу валяется никто его нет')
                print(res, sentence)

