from flask_restful import Resource
from models.user import UserModel

class Users(Resource):
    
    def get(self):
        return {'users' : [user.json() for user in UserModel.query.all().paginate(1,20)]}
        
class User(Resource):

    def get(self,name):
        user = UserModel.find_user_by_name(name)
        # call the class function
        if user: 
            return user.json() # if the User exists return the User 
        return {'message': 'User not found'}, 404  # else return User not found 
