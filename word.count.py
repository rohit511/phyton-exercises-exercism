import re
from collections import Counter
def count_words(sentence):
    # regex for all words and words with ' like "it's" and all digits
    regex = "(?<![^\W\d_])[^\W_]+(?:['.][^\W_]+)*(?![^\W\d_])"
    # Counter makes a special dictionary from counted items. use dict() to get normal dict
    return dict(Counter(re.findall(regex, sentence.lower())))