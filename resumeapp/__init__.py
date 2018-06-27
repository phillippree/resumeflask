from flask import Flask
from config import config
import os


def create_app(config_name):
    app = Flask(__name__,
                static_folder=os.path.join(os.path.dirname(__file__), r'../static'),
                template_folder=os.path.join(os.path.dirname(__file__), r'../templates'))
    app.config.from_object(config[config_name])

    from resumeapp.home import homeapp
    app.register_blueprint(homeapp)

    return app

