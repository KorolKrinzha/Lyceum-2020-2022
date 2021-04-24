import collections

#Это нам нужно для tf
def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        
        tf_text[i] = tf_text[i]/float(len(text))
    
    return tf_text

#Костыль для вывода текст в массив, так как мне было лень писать код самому...
def words(stringIterable):
    
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word

mylist = []
with open('text_for_test.txt', 'r') as myself:
    for word in words (myself):
        mylist.append (word)
        
tfword = input("Введите слово, частотность которого вы хотите посчитать ")  
     
a = compute_tf(mylist)
print("Частотность вашего слова равна ", a[tfword])

