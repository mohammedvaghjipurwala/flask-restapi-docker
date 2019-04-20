"""This is class Module"""
from datetime import datetime
from flask_restful import Resource,request
from models.entityClass import EntityClassModel

class EntityClass(Resource):
    """This is class"""

    def get(self, name):
        """returns values from class table"""
        entityClass = EntityClassModel.find_by_name(name)
        if entityClass:
            return entityClass.json()
        return {'message': 'entityClass not found'}, 404

    def post(self, name):
        """Creates values in class table"""
        if EntityClassModel.find_by_name(name):
            return {'message': 'A entityClass with the name {} already exists'.format(name)}, 400
        created_on = str(datetime.now())
        updated_on = str(datetime.now())
        entityClass = EntityClassModel(name, created_on, updated_on)
        try:
            entityClass.save_to_db()
        except:
            return {'message': 'An error occurred while creating the entityClass.'}, 500
        return entityClass.json(), 201

    def delete(self, name):
        """Deletes values from Class table"""
        entityClass = EntityClassModel.find_by_name(name)
        if entityClass:
            entityClass.delete_from_db()
        return {'message': 'EntityClass deleted'}

    def put(self,name):
        """Updates data in classes table"""
        entityClass = EntityClassModel.find_by_name(name)
        created_on = str(datetime.now())
        updated_on = str(datetime.now())
        if entityClass is None:
            entityClass = EntityClassModel(name, created_on, updated_on)
        else:
            entityClass.updated_on = str(datetime.now())
        entityClass.save_to_db()
        return entityClass.json()


class EntityClassList(Resource):
    """This class returns all available class from DB"""
    
    def get(self):
        """return all classes"""
        return {'entityClasss': [entityClass.json() for entityClass in EntityClassModel.query.all()]}
