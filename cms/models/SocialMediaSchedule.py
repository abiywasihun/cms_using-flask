from cms import db

class SocialMediaSchedule(db.Model):
    __tablename__ = 'SocialMediaSchedule'
     
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    time = db.Column(db.String())
    date = db.Column(db.String())
    permalink = db.Column(db.String())
    excerpt = db.Column(db.String())
    status = db.Column(db.Integer)
    review = db.Column(db.Integer)
    author = db.Column(db.Integer)

    def __init__(self, 	title,time,date,permalink, excerpt, status,review,author):
        self.title = title
        self.time = time
        self.date = date
        self.permalink = permalink
        self.excerpt = excerpt
        self.status = status
        self.review = review
        self.author = author

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'title': self.title,
            'time': self.time,
            'date':self.date,
            'permalink':self.permalink,
            'excerpt':self.excerpt,
            'status':self.status,
            'review':self.review,
            'author':self.author
        }