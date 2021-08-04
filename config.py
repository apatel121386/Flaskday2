import os

from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# Windows- C:\Users\Ankit\Documents\CodingTemple-June-2021\Week6\day2.2\intro_to_flask_jun

class Config:
    SECRET_KEY = 'you-will-never-know-this-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False