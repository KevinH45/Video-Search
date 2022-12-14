import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from extensions import model
from sentence_transformers import util
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

def semanticSearch(query,docs):

    queryEmb = model.encode(query)
    docsEmb = model.encode(docs)

    scores = util.cos_sim(queryEmb, docsEmb)[0].cpu().tolist()

    scores = list(zip(docs, scores, docsEmb))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return scores[0][0]

def findSimilarity(query, s2, vect):

    s2 = s2.lower()
    vector2 = vect.transform([s2])

    return round(cosine_similarity(query, vector2)[0][0] * 100, 2)
