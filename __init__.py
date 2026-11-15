from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    Talisman(
        app,
        force_https=False,
        content_security_policy=None
    )
    CORS(app)
    return app
