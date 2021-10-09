import re

def words(stringIterable):
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word
            
text1 = []
text2 = []
text3 = []
text4 = []
text5 = []
text6 = []
text7 = []

with open('Garri_Potter_I_Dary_Smerti.txt', 'r', newline = '') as file:
    print(type(file))
       
    regex_num = re.compile('Гарр\w*\b')
    s = regex_num.findall(str(text1))
    
print(s)
