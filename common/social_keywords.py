from common.stopwords import STOPWORDS
from collections import Counter
import itertools


def get_keywords(posts):
    words = list(itertools.chain(
        *[list(set(post.text.lower().split())) for post in posts]))
    tokens = sorted(Counter(words).items(), key=lambda x: x[1], reverse=True)
    keywords = []
    for token in tokens:
        if (token[0] not in STOPWORDS and token[0].isalpha()):
            keywords.append(token)
        if (len(keywords) == 20):
            break
    keywords = dict(keywords)
    return [{'key': kw, 'value': keywords[kw]/len(posts)} for kw in keywords]
