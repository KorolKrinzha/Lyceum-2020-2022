import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer 


#nltk.download('punkt') #Опционально
#nltk.download('stopwords')

#text = ''' 
#Ходят по земле с инструментами, маленькими метелочками и кисточками люди и отыскивают места обитания 
#удивительных животных динозавров, живших миллионы лет назад. Никто никогда их не видел, но в горных породах сохранились их кости. 
#Ученые-палеонтологи раскапывают, промывают и восстанавливают скелет, а потом воссоздают внешний вид динозавра. 
#Это долгая и скрупулезная работа, ведь за миллионы лет кости стали хрупкими. 
#'''

#text = '''«Пуськи бятые» — цикл «лингвистических сказок» Людмилы Петрушевской, написанных в разные годы её творчества. 
#Первая из них, с таким же названием, была написана в 1984 году и впервые опубликована тогда же в «Литературной газете».''' 

original_text_name = 'To_Kill_a_Mockingbird.txt'
result_text_name = "Results.txt"

with open(original_text_name, 'r') as file:
    text = file.read().replace('\n', '')

download_stopwords = stopwords.words('russian') #стоп-слова

stop_text = []

tokens = word_tokenize(text) #разбиение на слова
for i in tokens:
    if i not in download_stopwords:
        stop_text.append(i)

#tok_sent = sent_tokenize(text) #разбиение на предложения

stemsPorter = []
porter = PorterStemmer()
for w in tokens:
    a = w
    w = porter.stem(w)
    if w != "":
        stemsPorter.append(w)
        




#stems = []
#stemmer = SnowballStemmer("russian")     #Стеммер Snowball
#for token in tokens:
#    token = stemmer.stem(token)
#    if token != "":
#        stems.append(token)

#print("word_tokenize:", tokens)
#print("sent_tokenize:", tok_sent)
print("stems:", stemsPorter)
