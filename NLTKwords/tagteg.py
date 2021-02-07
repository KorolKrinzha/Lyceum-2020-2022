import nltk
import pymorphy2
import csv
morph = pymorphy2.MorphAnalyzer()



#==================Я НЕ МОГ ОТКРЫТЬ НОРМАЛЬНО ТЕКСТОВЫЙ ФАЙЛ ИЗ-ЗА КОДИРОВКИ, ПОЭТОМУ ВОСПОЛЬЗОВАЛСЯ CSV КОСТЫЛЕМ==============#
with open('lyrics.txt', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    
    rows = list(reader)
    

#==================ПРОДОЛЖЕНИЕ КОСТЫЛЯ: ROWS ЭТО МАССИВ СО СЛОВАРЯМИ ВНУТРИ. КЛЮЧ - ПЕРВАЯ СТРОЧКА ВО ВСЕХ ЗНАЧЕНИЯХ ПОЧЕМУ-ТО==============#

data = ""

for k in rows:
    
    
    for v, s in k.items():
        
        data+=s+" "



#==================ТЕПЕРЬ В СТРОЧКУ DATA МЫ ЗАПИСАЛИ ВСЕ ЗНАЧЕНИЯ СЛОВАРЯ И МОЖЕМ АНАЛИЗИРОВАТЬ ТЕКСТ С ПОМОЩЬЮ NLTK И PYMORPHY==============#    





#with open('lyrics.txt', 'r') as file:
#    data = file.read().replace('\n', ' ')



print (nltk.pos_tag(data.split()))


text_split = data.split(" ")

morph = pymorphy2.MorphAnalyzer()

for a in text_split:
	parse = morph.tag(a)[0]
	
	
	print (a, parse)
