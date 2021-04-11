from flask_restplus import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
from app.v1 import v1_api
from ..models.product import Product

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    products = relationship("Product", back_populates="category")


    category_resource_model= v1_api.model('Category', {
        'id': fields.Integer(readOnly=True, description='The category unique identifier. ReadOnly.'),
        'title': fields.String(required=True, description='The category name'),
    })
    
    
    products_resource_model = v1_api.inherit('products resource model', category_resource_model, {
        'products' :  fields.List(fields.Nested(Product.product_resource_model))
    })
