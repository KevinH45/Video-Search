from flask import Flask
from flask_restful import Api
from config import Config
from resources.base import QueryResource, VideoResource
from extensions import db


def register_extensions(app):
    db.sync()


def create_app():
    app = Flask("aE5tSQPC51AFDUzOE3U3t5Ddz")
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_resources(app):
    api = Api(app)

    api.add_resource(QueryResource, "/api/query")
    api.add_resource(VideoResource, "/api/videos")


if __name__ == '__main__':
    app = create_app()
    app.run()
