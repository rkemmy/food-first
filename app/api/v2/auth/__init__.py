from flask import Blueprint
from .auth import Signup, Login

auth_blueprint = Blueprint('auth', __name__)