from flask_restful import Resource, reqparse
from models.user import User

class Users(Resource):
    
    def get(self):
        return {'users' : [user.json() for user in User.query.all()]}
        
class User(Resource):
    def get(self,name):
        user = User.find_user_by_name(name) # call the class function
        if user: 
            return user.json() # if the movie exists return the movie 
        return {'message': 'User not found'}, 404  # else return Movie not found 
