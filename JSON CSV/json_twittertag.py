import json
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
twi = twitter_samples.strings('negative_tweets.json')
tokens = twitter_samples.tokenized('negative_tweets.json')
postags = pos_tag_sents(tokens)
json.dumps(postags)
print(postags)