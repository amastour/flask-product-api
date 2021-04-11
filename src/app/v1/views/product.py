from flask_restplus import Resource, Namespace

from app import db
from app.v1 import v1_api
from ..models.product import Product as ProductModel
from ..controllers.product import create_product, update_product, delete_product, get_product

product_ns = Namespace('product', description='Product operations')


@product_ns.route('/')
class ProductList(Resource):
    @product_ns.marshal_with(ProductModel.product_resource_model)
    def get(self):
        """Get Products list"""
        prod = get_product()
        return prod

    @product_ns.expect(ProductModel.product_resource_model, validate=True)
    @product_ns.marshal_with(ProductModel.product_resource_model)
    
    def post(self):
        """Create a new product"""
        prod = create_product(v1_api.payload)
        return prod, 201


@product_ns.route('/<int:id>')
class Product(Resource):
    @product_ns.response(404, 'Product not found or you don\'t have permission to view it')
    @product_ns.marshal_with(ProductModel.product_resource_model)
    def get(self, id):
        """Get one task"""
        prod = get_product(id=id)
        return prod

    @product_ns.response(404, 'Product not found or you don\'t have permission to edit it')
    @product_ns.response(201, 'Product successfully updated.')
    @product_ns.expect(ProductModel.product_resource_model, validate=True)
    @product_ns.marshal_with(ProductModel.product_resource_model)
    def put(self, id):
        """Get one Product"""

        prod = update_product(id, v1_api.payload)

        return prod

    @product_ns.response(404, 'Product not found or you don\'t have permission to delete it')
    @product_ns.response(204, 'Product deleted')
    def delete(self, id):
        """Delete one Product"""
        prod = delete_product(id=id)

        return '', 204
