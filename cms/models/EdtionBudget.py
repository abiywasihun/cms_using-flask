from cms import db
from datetime import datetime
class Column(db.Model):
    __tablename__ = 'planner'
     
    id = db.Column(db.Integer, primary_key=True)
    total_page = db.Column(db.String())
    number = db.Column(db.String())
    volume = db.Column(db.String())
    total_advertisement = db.Column(db.String())
    no_of_color_pages = db.Column(db.String())
    created_by = db.Column(db.String())
    created_at= db.Column('created_at', db.DateTime)

    def __init__(self, total_page,number,volume,total_advertisement, no_of_color_pages):
        self.total_page = total_page
        self.number = number
        self.volume = volume
        self.total_advertisement = total_advertisement
        self.no_of_color_pages = no_of_color_pages
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'total_page': self.total_page,
            'number': self.number,
            'volume':self.volume,
            'total_advertisement':self.total_advertisement,
            'no_of_color_pages':self.no_of_color_pages,
            'created_by':self.created_by,
            'created_at':self.created_at
        }