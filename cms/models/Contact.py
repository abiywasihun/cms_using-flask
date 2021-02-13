from cms import db
from datetime import datetime

class Contact(db.Model):
    __tablename__ = 'Contact'
     
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String())
    title = db.Column(db.String())
    firstName = db.Column(db.String())
    lastName = db.Column(db.String())
    cellPhone = db.Column(db.String())
    workPhone = db.Column(db.String())
    email = db.Column(db.String())
    description = db.Column(db.String())
    remark = db.Column(db.String())
    created_at= db.Column('created_at', db.DateTime)

 
    def __init__(self, organization,title,firstName,lastName, cellPhone	, workPhone,email,description,remark):
        self.organization = organization
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.cellPhone	 = cellPhone
        self.workPhone = workPhone
        self.email = email
        self.description = description
        self.remark = remark
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'organization': self.organization,
            'title': self.title,
            'firstName':self.firstName,
            'lastName':self.lastName,
            'cellPhone':self.cellPhone,
            'workPhone':self.workPhone,
            'email':self.email,
            'description':self.description,
            'remark':self.remark,
            'created_at':self.created_at
        }