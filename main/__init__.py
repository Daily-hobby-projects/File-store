from flask import Flask,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_fontawesome import FontAwesome
from flask_login import LoginManager
from os.path import dirname,realpath,join
import os
from .extensions.database import db
from .models.images import Image
from .config import Config,DevConfig,TestConfig
from .ui.routes import app_bp


def create_app():
    app=Flask(__name__,static_folder='static')
    

    app.config.from_object(DevConfig)

    app.register_blueprint(app_bp,url_prefix='/')

    fa=FontAwesome(app)

    db.init_app(app)

    return app