from flask import Blueprint

from .orders import PostOrder, SpecificOrder

orderly_blueprint = Blueprint('orderly', __name__)