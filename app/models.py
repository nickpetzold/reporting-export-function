from sqlalchemy import Column, Integer, JSON, String, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from app import db


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    type = db.Column(db.Text)


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    url = db.Column(db.String)
    result_all = db.Column(db.JSON)
    result_no_stop_words = db.Column(db.JSON)
