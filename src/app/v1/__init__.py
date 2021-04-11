from flask import Blueprint
from flask_restplus import Api

v1_blueprint = Blueprint('v1_blueprint', __name__)
v1_api = Api(v1_blueprint,
             title='Product API',
             version='1.0',
             description='simple api for learn')

from .views.product import product_ns
from .views.category import category_ns

v1_api.add_namespace(category_ns)
v1_api.add_namespace(product_ns)
