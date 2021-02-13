from cms import db

class OpEd(db.Model):
    __tablename__ = 'OpEd'
     
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String())
    content = db.Column(db.String())
    category = db.Column(db.String())
    excerpt = db.Column(db.String())
    date = db.Column(db.String())
    writtenBy = db.Column(db.String())

    def __init__(self, headline,content,category,excerpt, date, writtenBy):
        self.headline = headline
        self.content = content
        self.category = category
        self.excerpt = excerpt
        self.date = date
        self.writtenBy = writtenBy

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'headline': self.headline,
            'content': self.content,
            'category':self.category,
            'excerpt':self.excerpt,
            'date':self.date,
            'writtenBy':self.writtenBy
        }