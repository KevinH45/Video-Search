import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Stemmer

english_stemmer = Stemmer.Stemmer('en')


class CustomTfidfVectorizer(TfidfVectorizer):
    # Credit to https://stackoverflow.com/questions/26195699/sklearn-how-to-speed-up-a-vectorizer-eg-tfidfvectorizer
    # For providing this snippet of code
    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: english_stemmer.stemWords(analyzer(doc))

def preprocessText(s):

    s = s.lower()
    res = re.sub("[^a-zA-Z]", " ", s)

    return res

def findSimilarity(query, s2, vect):

    s2 = s2.lower()
    vector2 = vect.transform([s2])

    return round(cosine_similarity(query, vector2)[0][0] * 100, 2)
