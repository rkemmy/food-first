from flask import Blueprint

from .orders import PostOrder, SpecificOrder, UserHistory

orderly_blueprint = Blueprint('orderly', __name__)