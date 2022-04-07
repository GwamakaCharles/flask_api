import os

from flask import Flask
from flask_restful import  Api 

from resources.user import User, Users

from db import db
app = Flask(__name__)
# app.config.from_object(BaseConfig)
api = Api(app)

uri = os.getenv("DATABASE_URL") 
if uri: # or other relevant config var
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

else:
    uri = 'sqlite:///data.db'

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_tables():
    db.create_all()

# api.add_resource(Users, '/users')

@api.resource(Users, '/users')
class Foo(Resource):
    def get(self):
        return 'Hello, World!'
        
api.add_resource(User, '/user/<string:name>')


db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)