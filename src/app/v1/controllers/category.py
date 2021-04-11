from ..models.category import Category as CategoryModel
from app import db

def get_category(category_id=None):
    
    if category_id is None:
        cat = CategoryModel.query.all()
    else:
        cat = CategoryModel.query.filter_by(id=category_id).first_or_404()
    
    return cat

def create_category(data):
    title = data['title']

    cat = CategoryModel(title= title, active= True)
    db.session.add(cat)
    db.session.commit() 
    return cat

def update_category(category_id,data):
    cat = CategoryModel.query.filter_by(id=category_id).first_or_404()

    if 'title' in data:
        cat.title= data['title']

    if 'active' in data:
        cat.active= data['active']

    db.session.add(cat)
    db.session.commit()

    return cat

def delete_category(category_id):
    cat = CategoryModel.query.filter_by(id=category_id).first_or_404()

    cat.active= False

    db.session.add(cat)
    db.session.commit()

    return cat
    