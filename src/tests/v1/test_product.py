import unittest
from flask import json

from app import create_app, db

class ProductTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app(config_type='test')
        self.client = create_app(config_type='test').test_client()
        with self.app.app_context():
            db.create_all()
    

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
    
    def create(self, title, price, description=""):
        return self.client.post('/api/v1/product/', data=json.dumps({
            'title': title,
            'description': description,
            'price': price
        }), content_type='application/json')
    
    def update(self, id, title, price, description=""):
        return self.client.put('/api/v1/product/{}'.format(id), data=json.dumps({
            'id': id,
            'title': title,
            'description': description,
            'price': price
        }), content_type='application/json')
    
    def delete(self, id):
        return self.client.delete('/api/v1/product/{}'.format(id),
         content_type='application/json')
    
    def view_one(self, id):
        return self.client.get('/api/v1/product/',
         data=json.dumps({'id': id}),
         content_type='application/json')


    def view_list(self):
        return self.client.get('/api/v1/product/',
         content_type='application/json')




##############################################################
#                                                            #
#                           TEST CASES                       #
#                                                            #
##############################################################

    def test_create_than_view(self):
        rs = self.create('banana', 5, 'fruit')
        assert b'banana' in rs.data

        rs = self.view_one(id=1)
        assert b'banana' in rs.data
    
    def test_create_than_list(self):
        rs = self.create('apple', 5, 'fruit')
        assert b'apple' in rs.data
        rs = self.create('banana', 3, 'fruit')
        assert b'banana' in rs.data

        rs = self.view_list()
        assert len(rs.get_json()) == 2
    
    def test_create_than_update(self):
        rs = self.create('banana', 5, 'fruit')
        assert b'banana' in rs.data

        id_banana = rs.get_json().get('id')
        rs = self.update(id_banana, 'banana', 3, 'fruit')
        assert b'3' in rs.data
    
    def test_create_than_delete(self):
        rs = self.create('banana', 5, 'fruit')
        assert b'banana' in rs.data

        id_banana = rs.get_json().get('id')
        rs = self.delete(id_banana)
        assert b'banana' not in rs.data




    

