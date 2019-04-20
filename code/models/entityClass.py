from db import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class EntityClassModel(db.Model):
    """This is Class Model"""
    __tablename__='entityClasses'

    id =db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), default=uuid4)
    name=db.Column(db.String(80))
    created_on = db.Column(db.String(80))
    updated_on = db.Column(db.String(80))
    entityStudents = db.relationship('EntityStudentModel', lazy='dynamic')

    def __init__(self, name, created_on, updated_on):
        """This is initialize method"""
        self.name=name
        self.created_on = created_on
        self.updated_on = updated_on

    def json(self):
        """This method return json data"""
        return {'name':self.name,'entityStudents':[entityStudent.json() for entityStudent in self.entityStudents.all()],'created_on':self.created_on[:19],'updated_on':self.updated_on[:19]}

    @classmethod
    def find_by_name(cls, name):
        """This method finds first name from the database"""
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        """This method saves data in DB"""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """This method deletes values from DB"""
        db.session.delete(self)
        db.session.commit()
