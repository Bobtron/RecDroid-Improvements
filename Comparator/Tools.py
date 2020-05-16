from nltk.corpus import stopwords

import re

regex = re.compile('[^a-z\s0-9]')
# First parameter is the replacement, second parameter is your input string
# regex.sub('', 'ab3d*E')
# Out: 'abdE'

stop_words = stopwords.words('english')

def preprocess(sentence):
    if sentence[-1] == '\n':
        sentence = sentence[:-1]
    return [w for w in regex.sub('', sentence.lower()).split() if w not in stop_words]
