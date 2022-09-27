from flask_restful import Resource
from flask import request
from http import HTTPStatus
from query import findRelatedVideo, findSentences
from extensions import db
from youtube_transcript_api import YouTubeTranscriptApi

class QueryResource(Resource):

    def post(self):

        data = request.get_json()

        try:
            query = data["query"]
        except KeyError:
            return {"msg": "Your JSON is formatted wrong :("}, HTTPStatus.BAD_REQUEST

        relContent = findRelatedVideo(query, db)
        times = findSentences(query, relContent)

        return  {"msg": "Success", "video_id": relContent["title"], "times": times}, HTTPStatus.OK

class VideoResource(Resource):

    def post(self):

        data = request.get_json()

        try:
            vid = data["video"]
        except KeyError:
            return {"msg": "Your JSON is formatted wrong :("}, HTTPStatus.BAD_REQUEST

        transcript = YouTubeTranscriptApi.get_transcript(vid)

        text = [x["text"].replace("\n", " ") for x in transcript]

        db.shelf("prodDB").insert({
            'title': vid,
            'transcript': transcript,
            'content': text,
            'rawtext': ' '.join(text),
        }).run()

        return {"msg": "Entered into db"}, HTTPStatus.CREATED


