from nlp import findSimilarity, CustomTfidfVectorizer
import shelfquery


def findRelatedVideo(query, db):
    vect = CustomTfidfVectorizer()
    query = vect.fit_transform([query])
    res = db.shelf('prodDB').filter(lambda x: True).run()

    maxSim = float("-inf")
    relContent = None
    for i in res:

        sim = findSimilarity(query, i["rawtext"], vect)

        if sim > maxSim:
            maxSim, relContent = sim, i

    return relContent


def findSentences(query, relContent):

    vect = CustomTfidfVectorizer()
    query = vect.fit_transform([query])
    sentences = relContent["rawtext"].split(".")
    timedText = relContent["transcript"]

    res = []
    idx = 0
    for i in sentences:

        sim = findSimilarity(query, i, vect)

        if sim > 60:
            res.append((timedText[idx]['start'], timedText[idx]
                       ["duration"]+timedText[idx]['start']))

        idx += 1

    return res
