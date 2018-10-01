from flask import Blueprint
from .auth import Signup

auth_blueprint = Blueprint('auth', __name__)