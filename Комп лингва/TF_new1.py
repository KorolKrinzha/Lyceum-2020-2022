import collections
#https://superuser.com/questions/621720/remove-empty-lines-and-spaces-in-notepad
#http://nlpx.net/archives/57
def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        
        tf_text[i] = tf_text[i]/float(len(text))
    
    return tf_text

#https://stackoverflow.com/questions/19720311/how-to-split-a-text-file-to-its-words-in-python
def words(stringIterable):
    
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word

mylist = []
with open('new 1.txt', 'r') as myself:
    for word in words (myself):
        mylist.append (word)
print (compute_tf(mylist), sep='\n')
