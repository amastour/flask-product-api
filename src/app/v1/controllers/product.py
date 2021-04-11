from ..models.product import Product as ProductModel
from ..models.category import Category as CategoryModel
from app import db


def get_product(product_id=None):
    
    if product_id is None:
        prod = ProductModel.query.all()
    else:
        prod = ProductModel.query.filter_by(id=product_id).first_or_404()
    
    return prod


def create_product(data):

    title = data['title']
    description = data['description']
    price = data['price']
    category_id = data['category_id']

    cat = CategoryModel.query.filter_by(id=category_id).first_or_404()
    prod = ProductModel(title= title, description= description, price= price, category= cat)
    db.session.add(prod)
    db.session.commit() 
    return prod

def update_product(product_id,data):
    prod = ProductModel.query.filter_by(id=product_id).first_or_404()
    
    if 'title' in data:
        prod.title= data['title']

    if 'active' in data:
        prod.active= data['active']

    if 'category_id' in data:
        category_id = data['category_id']
        cat = CategoryModel.query.filter_by(id=category_id).first_or_404()
        prod.category = cat

    db.session.add(prod)
    db.session.commit()

    return prod

def delete_product(product_id):
    prod = ProductModel.query.filter_by(id=product_id).first_or_404()

    prod.active= False

    db.session.add(prod)
    db.session.commit()

    return prod
    