from nlp import findSimilarity, CustomTfidfVectorizer, preprocessText, semanticSearch
import shelfquery


def findRelatedVideo(query, db):
    vect = CustomTfidfVectorizer()
    query = vect.fit_transform([preprocessText(query)])
    res = db.shelf('prodDB').filter(lambda x: True).run()

    maxSim = float("-inf")
    relContent = None
    for i in res:

        sim = findSimilarity(query, preprocessText(i["rawtext"]), vect)

        if sim > maxSim:
            maxSim, relContent = sim, i

    return relContent


def findSentences(query, relContent):

    query = preprocessText(query)
    sentences = [x["text"] for x in relContent["transcript"]]
    timedText = relContent["transcript"]

    answer = semanticSearch(query, sentences)
    res = None
    for i in timedText:

        if i["text"] == answer:
            res = i["start"]
            tmp = i["duration"]
            break


    return [res, res+tmp]
