from flask_restful import Resource
from flask import request
from werkzeug.security import check_password_hash
from ..models import User

class Signup(Resource):
    def post(self):
        ''' Add a new user '''
        data = request.get_json()

        username = data['username']
        email = data["email"]
        password = data['password']

        user = User(username, email, password)

        user.add()

        return {'message': 'Account created successfully'}, 201

