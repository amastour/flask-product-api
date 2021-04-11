from flask_restplus import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app import db
from app.v1 import v1_api


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250))
    price = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean(), default=False)

    category_id = db.Column(db.Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="products")

    product_resource_model = v1_api.model('Product', {
        'id': fields.Integer(readOnly=True, description='The product unique identifier. ReadOnly.'),
        'title': fields.String(required=True, description='The product name'),
        'description': fields.String(description='Bla bla bla'),
        'price': fields.Integer(required=True, description='The price of product'),
        'category_id': fields.Integer(attribute='category.id'),
        'category': fields.String(attribute='category.title'),
    })

