from flask_restplus import Resource, Namespace

from app.v1 import v1_api
from ..models.category import Category as CategoryModel
from ..controllers.category import get_category, create_category, update_category, delete_category

category_ns = Namespace('category', description='Category operations')


@category_ns.route('/')
class CategoryList(Resource):
    @category_ns.marshal_with(CategoryModel.category_resource_model)
    def get(self):
        """Get Categorys list"""
        cats = get_category()
        return cats

    @category_ns.expect(CategoryModel.category_resource_model, validate=True)
    @category_ns.marshal_with(CategoryModel.category_resource_model)
    def post(self):
        """Create a new category"""
        cat = create_category(v1_api.payload)
        return cat, 200


@category_ns.route('/<int:id>')
class Category(Resource):
    @category_ns.response(404, 'Category not found or you don\'t have permission to view it')
    @category_ns.marshal_with(CategoryModel.products_resource_model)
    def get(self, id):
        """Get one task"""
        cat = get_category(id)
        return cat

    @category_ns.response(404, 'Category not found or you don\'t have permission to edit it')
    @category_ns.response(201, 'Category successfully updated.')
    @category_ns.expect(CategoryModel.category_resource_model, validate=True)
    @category_ns.marshal_with(CategoryModel.category_resource_model)
    def put(self, id):
        """Get one Category"""

        cat = update_category(id, v1_api.payload)
        return cat

    @category_ns.response(404, 'Category not found or you don\'t have permission to delete it')
    @category_ns.response(204, 'Category deleted')
    def delete(self, id):
        """Delete one Category"""
        delete_category(id)

        return '', 204
