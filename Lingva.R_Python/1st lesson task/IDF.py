import math

def compute_idf(word, corpus):
    if corpus.count(word)==0 and len (corpus)!=4: #очень коряво и неправильно, но работает:( Четыре - длина текстс,
        #т.е. если бы у нас не было второго условия, то каждый раз он был писал ноль, так как элементы массива текстс - это другие массивы.
        #поэтому мне нужно еще разработать защиту, котороая будет работать, например, при print (compute_idf('exist', texts))
        #Сейчас программа выдает ошибку division by zero, что логично, так как exist встречается ноль раз во всех четырех текстах
        #а так все остальное вроде норм
        return 0
    else:     
        
        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))
        

def words(stringIterable):
    
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word


new2 = []
new3 = []
new4 = []
new5 = []



with open('new 2.txt', 'r') as myself:
    for word in words (myself):
        new2.append (word)
with open('new 3.txt', 'r') as myself:
    for word in words (myself):
        new3.append (word)
with open('new 4.txt', 'r') as myself:
    for word in words (myself):
        new4.append (word)
with open('new 5.txt', 'r') as myself:
    for word in words (myself):
        new5.append (word)




texts = [new2, new3, new4, new5]
print (texts)

print (compute_idf('exoist', texts))
