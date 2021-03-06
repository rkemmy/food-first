import re

from flask_restful import Resource
from flask import request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from ..models import User

class Signup(Resource):
    def post(self):
        ''' Add a new user '''
        try:

            data = request.get_json()

            username = (data['username']).lower()
            email = (data["email"]).lower()
            password = data['password']
            confirm_password = data['confirm_password']
        
        except Exception as e:
            return ({'message': str(e)}), 400

        if type(data['username']) != str or type(data['email']) != str or type(data['password']) != str:
            return {'message': 'Valid username, email and password should be a str'}

        if not re.match('^[a-zA-Z]{6,20}$', username):
            return {'message':'Valid username should be alphabetic, between 6 and 20 characters'}, 400

        if password != confirm_password:
            return {'message': 'Passwords do not match'}, 400

        if not re.match(r"^[a-z0-9@.]+@[^@]+\.[^@]+$", email):
            return {'message': 'Valid email should be alphanumeric with the @ and . symbol'}, 400

        if not re.match("^[a-zA-Z0-9$]{8,20}$", password):
            return {'message':'Valid password should be alphanumeric, between 8 to 20 characters'}, 400
        
        if User().get_user_by_username(username):
            return {'message': 'username already in use'}, 400
        
        if User().get_user_by_email(email):
            return {'message': 'email already in use'}, 400


        user = User(username, email, password)

        user.add()

        return {'message': 'Account created successfully'}, 201

        

class Login(Resource):
    def post(self):
        ''' Existing user can login '''
        try:
            data = request.get_json()

            username = data['username']
            password = data['password']

        except:
            return {'message': 'Json data empty or invalid'}, 200

        user = User().get_user_by_username(username)

        if type(data['username']) != str or type(data['password']) != str:
            return {'message': 'please input string data'}

        elif not user:
            return {'message': 'user not found'}, 404

        elif not check_password_hash(user.password, password):
            return {'message': 'Wrong password'}, 400

        token = create_access_token(identity=(username, user.is_admin ))
        return {
            'token': token,
            'message': f'You were successfully logged in {username}',
            'admin': user.is_admin
        }, 200
