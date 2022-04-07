from db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))

    def __init__(self,name):
        self.name = name        

    def json(self):
        return {'name': self.name}