import nltk
#nltk.download('twitter_samples') # already downloaded
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
#print (twitter_samples.fileids()) -->
# ['negative_tweets.json', 'positive_tweets.json', 'tweets.20150430-223406.json']
tweets_negative = twitter_samples.strings('negative_tweets.json')
tokens = twitter_samples.tokenized('negative_tweets.json')
postags = pos_tag_sents(tokens)
print (postags)