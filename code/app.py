#!/usr/bin/env python3
"""REST API"""
import os
from flask import Flask
from flask_restful import Api
from resources.entityStudent import EntityStudent, EntityStudentList
from resources.entityClass import EntityClass, EntityClassList

APP = Flask('__name__')
APP.config['SECRET_KEY'] = 'mustafanw'
APP.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user='postgres',
        passwd='qwerty52',
        host='localhost',
        port=5432,
        db='data')
APP.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False

API = Api(APP)

@APP.before_first_request
def create_tables():
    """Creates tables in the database"""
    db.create_all()

API.add_resource(EntityStudent, '/student/<string:name>')
API.add_resource(EntityStudentList, '/students')
API.add_resource(EntityClass, '/class/<string:name>')
API.add_resource(EntityClassList, '/classes')

if __name__ == '__main__':
    from db import db
    db.init_app(APP)
    APP.run(port=4999,debug=True)
