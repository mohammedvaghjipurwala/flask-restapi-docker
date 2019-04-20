"""Entity Student Model"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from db import db

class EntityStudentModel(db.Model):
    """ This is Student Model"""
    __tablename__='entityStudents'

    id =db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), default=uuid4)
    name=db.Column(db.String(80))
    entityClass_id = db.Column(db.Integer, db.ForeignKey('entityClasses.id'))
    created_on = db.Column(db.String(80))
    updated_on = db.Column(db.String(80))
    entityClass = db.relationship('EntityClassModel')

    def __init__(self, name, created_on, updated_on, entityClass_id):
        """This is initialize method"""
        self.name = name
        self.created_on = created_on
        self.updated_on = updated_on
        self.entityClass_id = entityClass_id

    def json(self):
        """This method returns json data"""
        return {'name':self.name,'created_on':self.created_on[:19],'updated_on':self.updated_on[:19]}

    @classmethod
    def find_by_name(cls, name):
        """This method finds name of student from student table"""
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        """This method saves student data in database"""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """This method deletes student data from database"""
        db.session.delete(self)
        db.session.commit()
