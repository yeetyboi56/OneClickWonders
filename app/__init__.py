import os

from flask import Flask
from pymongo import MongoClient

from app.routes.index import index_route
from app.routes.login import login_route
from app.routes.register import register_route


def create_app():
    app = Flask(__name__)

    app.secret_key = os.environ["SECRET_KEY"]

    app.db_client = MongoClient(os.environ["MONGODB_URI"])
    app.db = app.db_client.get_default_database()

    # Register all blueprints
    app.register_blueprint(index_route)
    app.register_blueprint(login_route)
    app.register_blueprint(register_route)

    return app
