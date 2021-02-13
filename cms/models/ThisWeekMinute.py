from cms import db

class ThisWeekMinute(db.Model):
    __tablename__ = 'ThisWeekMinute'
     
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    content = db.Column(db.String())
    number = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    author = db.Column(db.Integer)
    date = db.Column(db.String())
    draftID = db.Column(db.String())
    section = db.Column(db.String())
    status = db.Column(db.String())
    headline = db.Column(db.String())
    updated_at= db.Column('updated_at', db.DateTime)

    def __init__(self, category,content,number,volume, author, date,draftID,section,status,headline,updated_at):
        self.category = category
        self.content = content
        self.number = number
        self.volume = volume
        self.author = author
        self.date = date
        self.draftID = draftID
        self.section = section
        self.status = status
        self.headline = headline
        self.updated_at = updated_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'category': self.category,
            'content': self.content,
            'number':self.number,
            'volume':self.volume,
            'author':self.author,
            'date':self.date,
            'draftID':self.draftID,
            'section':self.section,
            'status':self.status,
            'headline':self.headline,
            'updated_at':self.updated_at

        }