''''
Shallow parsing (also chunking or light parsing)
is an analysis of a sentence which first identifies
constituent parts of sentences (nouns, verbs, adjectives, etc.)
and then links them to higher order units that have discrete grammatical meanings
(noun groups or phrases, verb groups, etc.).
'''
import nltk

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import json

result_dict = {}


with open('test.txt', 'r', encoding="utf-8") as data:
    text = data.read().replace('\n', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('   ', ' ')



def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))

    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk


def get_continuous_chunks_for_geo(text, label):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))

    continuous_chunk = []
    current_chunk = []

    for subtree in chunked:
        if type(subtree) == Tree and subtree.label() == label:
            current_chunk.append(" ".join([token for token, pos in subtree.leaves()]))
        if current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk



result_dict['Geolocation'] = get_continuous_chunks_for_geo(text, 'GPE')
result_dict['Names'] = get_continuous_chunks(text)
json_data = json.dumps(result_dict, indent=4)





with open('storyparser_result.json', 'w', encoding="utf-8") as data:
    data.write(json_data)





# Ссылки
# https://github.com/rohitjose/InformationExtraction
# https://stackoverflow.com/questions/24398536/named-entity-recognition-with-regular-expression-nltk
# https://nlp.stanford.edu/software/CRF-NER.shtml
# https://stackoverflow.com/questions/48660547/how-can-i-extract-gpelocation-using-nltk-ne-chunk

