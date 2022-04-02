import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)



lemmatizer = WordNetLemmatizer()

f = open('test.txt', 'r')
sentence = f.read()
f.close()

result = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sentence)]

file = open('test.txt','w')

for key in result:
    ans = str(key) + " "
    file.write(ans)

file.close()
