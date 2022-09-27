from youtube_transcript_api import YouTubeTranscriptApi
import shelfquery
db = shelfquery.db()
db.sync()

res = []
with open("ytbase.txt", "r") as f:

    s = f.readlines()
    for i in s:
        vid = i[32:].strip()
        transcript = YouTubeTranscriptApi.get_transcript(vid)


        text = [x["text"].replace("\n", " ") for x in transcript]

        db.shelf("prodDB").insert({
            'title': vid,
            'transcript': transcript,
            'content': text,
            'rawtext': ' '.join(text),
        }).run()


