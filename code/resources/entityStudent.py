"""This is STudent Module"""
from datetime import datetime
from flask_restful import Resource, reqparse, request
from models.entityStudent import EntityStudentModel

class EntityStudent(Resource):
    """This is student class"""

    def get(self, name):
        """returns student"""
        entityStudent=EntityStudentModel.find_by_name(name)
        if entityStudent:
            return entityStudent.json()
        return {'message':'entityStudent not found'}

    def post(self, name):
        """creates new student"""
        if EntityStudentModel.find_by_name(name):
            return {'message':'A entityStudent with name {} already exists.'.format(name)},400
        data= request.get_json()
        created_on = str(datetime.now())
        updated_on = str(datetime.now())
        entityStudent=EntityStudentModel(name, created_on, updated_on, data['entityClass_id'])
        try:
            entityStudent.save_to_db()
        except:
            return ("Error occur while inserting"),500
        return entityStudent.json() , 201

    def delete(self, name):
        """Deletes students"""
        entityStudent = EntityStudentModel.find_by_name(name)
        if entityStudent:
            entityStudent.delete_from_db()
            return ("Student Deleted")
        else:
            return (" Student not found")

    def put(self, name):
        """updates students"""
        data=request.get_json()
        entityStudent=EntityStudentModel.find_by_name(name)
        created_on = str(datetime.now())
        updated_on = str(datetime.now())
        entityClass_id = data['entityClass_id']
        if entityStudent is None:
            entityStudent = EntityStudentModel(name, entityClass_id, created_on, updated_on)
        else:
            entityStudent.updated_on = str(datetime.now())
            entityStudent.entityClass_id = entityClass_id
        entityStudent.save_to_db()
        return entityStudent.json()

class EntityStudentList(Resource):
    """This class returns all students"""

    def get(self):
        """retuns all students"""
        return {'entityStudents':[entityStudent.json() for entityStudent in EntityStudentModel.query.all()]}
