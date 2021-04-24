
###ЗАДАНИЕ###
#а) чему равно среднее число слов в предложении, а также в каком предложении больше всего односимвольных слов. 
#б) выберите любое #слово и посчитайте TF (частотность) термина X = (Количество раз, когда термин X встретился в тексте / количество всех слов в тексте) 


###ЗАДАНИЕ1###


dictimin = {}
with open('text_for_test.txt', encoding='utf-8') as f:
  f = f.read()
  text = f.replace('?', '.').replace('!', '.').replace('...', '.').replace('—', ' ')
  for sentence in text.split("."):
      dictimin[sentence] = len([j for j in sentence.split() if len(j)==1 ])
  length = text.split(' ')
  countword = text.count('.')
 
print("Среднее число слов в предложении ", len(length)/countword)

kostil = [(value, key) for key, value in dictimin.items()]
print ("В предложении ", max(kostil)[1], "больше всего односимвольных слов: ", max(kostil)[0], end = "\n") 

#Недочет: знаки такие как тире тоже учитываются...(



###ЗАДАНИЕ2###
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
   

print("Второе задание: ", end=  " \n ")   
tfword = input("Введите слово, частотность которого вы хотите посчитать ")  
     
a = compute_tf(mylist)
print("Частотность вашего слова равна ", a[tfword])

