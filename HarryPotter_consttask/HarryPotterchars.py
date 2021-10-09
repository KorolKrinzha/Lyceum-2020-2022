import csv
import re
from nltk.tokenize import RegexpTokenizer

character_one = "Гарри"
character_two = "Сириус"
character_three = "Гермиона"


with open('results.csv', 'w') as tables:
    writer = csv.writer(tables, delimiter=",")
    data = ["Персонаж", "Какие формы встречаются в каждой книге", "Предложения в книге"]
    writer.writerow(data)

books = ['Filosofsky_Kamen',
         'Taynaya_Komnata',
         'Uznik_Azkabana',
         'Kubok_Ognya',
         'Orden_Fenixa',
         'Dary_Smerti']


def get_forms(data):
    tokenizer = RegexpTokenizer(r'\w+')
    data = ' '.join(tokenizer.tokenize(data))
    regex_ref = re.compile("%s\S+" % character[0:-1])
    findings = regex_ref.findall(data)
    unique = set(findings)
    result = {books[i - 1]: ', '.join(unique)}
    return result


def get_uniques(data):
    common = {}

    tokenizer = RegexpTokenizer(r'\w+')
    data = tokenizer.tokenize(data)

    regex_ref = re.compile("%s\S+" % character[0:-1])
    findings = regex_ref.findall(' '.join(data))
    unique = list(set(findings))


    for i in unique:
        common[i]=  data.count(i)



    return common

with open('results.csv', 'a') as tables:
    writer = csv.writer(tables, delimiter=",")

    for character in [character_one, character_two, character_three]:

        for i in range(1, 6 + 1):
            text_name = 'texts/%s.txt' % i

            with open(str(text_name), 'r') as text:
                data = text.read()

                forms = get_forms(data)

                refs = get_uniques(data)
                data_result = [character, forms, refs]
                writer.writerow(data_result)
