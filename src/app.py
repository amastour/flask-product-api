from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
import datetime
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "product.db"))

# App Initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= database_file
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Product API',
    description='A simple Product API',
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#manager.add_command('db', MigrateCommand)


# Database table definition
class Product(db.Model):
    __tablename__ = "conference"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, description, timing, location):
        self.title = title
        self.description = description
        self.timing = timing
        self.location = location
        super(ConferenceM,self).__init__()


    def __repr__(self):
        return '<Conference %s>' % self.title


ns = api.namespace('Conference', description='Conference operations')

conf = api.model('Conference', {
    'id': fields.Integer(readonly=True, description='The conference unique identifier'),
    'title': fields.String(required=True, description='The conference title'),
    'description': fields.String(required=True, description='The conference details'),
    'date': fields.DateTime(required=True, description='The conference date'),
    'location': fields.String(required=True, description='The conference location')
})




@ns.route('/')
class ConferenceList(Resource):
    '''Shows a list of all Conferences, and lets you POST to add new tasks'''
    @ns.doc('list_Conferences')
    @ns.marshal_list_with(conf)
    def get(self):
        '''List all tasks'''
        return '', 200

    @ns.doc('create_Conference')
    @ns.expect(conf)
    @ns.marshal_with(conf, code=201)
    def post(self):
        '''Create a new task'''  
        print(api.payload)      
        return '', 201


@ns.route('/<int:id>')
@ns.response(404, 'Conference not found')
@ns.param('id', 'The task identifier')
class Conference(Resource):
    '''Show a single Conference item and lets you delete them'''
    @ns.doc('get_Conference')
    @ns.marshal_with(conf)
    def get(self, id):
        '''Fetch a given resource'''
        return '', 204

    @ns.doc('delete_Conference')
    @ns.response(204, 'Conference deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        #DAO.delete(id)
        return '', 204

    @ns.expect(conf)
    @ns.marshal_with(conf)
    def put(self, id):
        '''Update a task given its identifier'''
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
