import shelfquery
db = shelfquery.db()
db.sync()

res = db.shelf('prodDB').filter(lambda x: x["title"]=="cPeVsniB7b0").run()

print(res[0]["transcript"])
