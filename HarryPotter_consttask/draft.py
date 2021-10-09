import csv
import re
from nltk.tokenize import RegexpTokenizer

character_one = "Гарри"
character_two = "Сириус"
character_three = "Гермиона"
characters = [character_one, character_two, character_three]




with open('results.csv', 'w') as tables:
    writer = csv.writer(tables, delimiter=",")
    data=["Персонаж","Какие формы встречаются в каждой книге", "Предложения в книге"]
    writer.writerow(data)

# Названия книг. Надеюсь, в правильном порядке.... Ну если что, поправьте
books = ['Filosofsky_Kamen',
         'Taynaya_Komnata',
         'Uznik_Azkabana',
         'Kubok_Ognya',
         'Orden_Fenixa',
         'Dary_Smerti']

def get_forms(data):
    tokenizer = RegexpTokenizer(r'\w+')
    data = ' '.join(tokenizer.tokenize(data))

    # Немного несовершенная, но рабочая регулярка
    regex_ref = re.compile("%s\S+" % character[0:-1])

    # То, что регулярка нашла
    findings = regex_ref.findall(data)

    # Убираем поторяющиеся рез-ты
    unique = set(findings)
    # print(books[i-1],"=====>", ', '.join(unique)) #какой некрасивый костыль с названиями,
    # уж лучше я бы просто тексты нормально назвал...
    # Ну тоже норм, потом если что поправлю
    result = {books[i - 1]: ', '.join(unique)}
    return result



def get_uniques(data):
    tokenizer = RegexpTokenizer(r'\w+')
    data = ' '.join(tokenizer.tokenize(data))

    # Немного несовершенная, но рабочая регулярка
    regex_ref = re.compile("%s\S+" % character[0:-1])

    # То, что регулярка нашла
    findings = regex_ref.findall(data)

    # Убираем поторяющиеся рез-ты
    unique = set(findings)
    




for character in characters:


    for i in range (1, 6+1):

        text_name = 'texts/%s.txt'%i

        with open(str(text_name), 'r') as text, open('results.csv', 'a') as tables:

            #Обработка текста
            data = text.read()
            r = get_forms(data)
            print(r)

            #writer.writerow(data_result)




    
