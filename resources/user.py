from flask_restful import Resource, reqparse
from models.movie import User

class Users(Resource):
    
    def get(self):
        return {'users' : [user.json() for user in User.query.all()]}
        
