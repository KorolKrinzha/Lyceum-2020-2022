import nltk
from nltk import WordNetLemmatizer
wnl = WordNetLemmatizer()
print (wnl.lemmatize("running"))

print (wnl.lemmatize("running",pos="v"))


print (wnl.lemmatize("cool"))

print (wnl.lemmatize("cool",pos="n"))

print (wnl.lemmatize("meow"))

print (wnl.lemmatize("meow",pos="a"))
