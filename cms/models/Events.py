from cms import db
from datetime import datetime

class Events(db.Model):
    __tablename__ = 'Events'
     
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    venue = db.Column(db.String())
    date_from_date = db.Column(db.String())
    date_from_time = db.Column(db.String())
    date_to_date = db.Column(db.String())
    date_to_time = db.Column(db.String())
    contactFirstName = db.Column(db.String())
    contactLastName = db.Column(db.String())
    contactOfficeTel = db.Column(db.String())
    contactMobileNum = db.Column(db.String())
    contactEmail = db.Column(db.String())
    description = db.Column(db.String())
    createdBy = db.Column(db.String())
    created_at= db.Column('created_at', db.DateTime)

 
    def __init__(self, title,venue,date_from_date,date_from_time,date_to_date, date_to_time, contactFirstName, contactLastName,contactOfficeTel,contactMobileNum,contactEmail,description,createdBy):
        self.title = title
        self.venue = venue
        self.date_from_date = date_from_date
        self.date_from_time = date_from_time
        self.date_to_date = date_to_date
        self.date_to_time = date_to_time
        self.contactFirstName = contactFirstName
        self.contactLastName = contactLastName
        self.contactOfficeTel = contactOfficeTel
        self.contactMobileNum = contactMobileNum
        self.contactEmail = contactEmail
        self.description = description
        self.createdBy = createdBy
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'title': self.title,
            'venue': self.venue,
            'date_from_date':self.date_from_date,
            'date_from_time':self.date_from_time,
            'date_to_date':self.date_to_date,
            'date_to_time':self.date_to_time,
            'contactFirstName':self.contactFirstName,
            'contactLastName':self.contactLastName,
            'contactOfficeTel':self.contactOfficeTel,
            'contactMobileNum':self.contactMobileNum,
            'contactEmail':self.contactEmail,
            'description':self.description,
            'createdBy':self.createdBy,
            'created_at':self.created_at
        }