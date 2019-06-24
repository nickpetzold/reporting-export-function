
from app import db


class Report(db.Model):
    __tablename__ = 'reports'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    type = db.Column(db.Text)

    def __init__(self, type):
        self.type = type
