import os
from flask import Flask

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))  # app/
    template_dir = os.path.join(base_dir, 'templates')     # app/templates
    static_dir = os.path.join(base_dir, 'styles')          # app/styles

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    from app.routes import bp
    app.register_blueprint(bp)

    return app
