from cms import db

class WebsiteContent(db.Model):
    __tablename__ = 'WebsiteContent'
     
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    headline = db.Column(db.String())
    sub_headline = db.Column(db.String())
    article = db.Column(db.String())
    nutshell = db.Column(db.String())
    blurb = db.Column(db.String())
    pullout = db.Column(db.String())
    author = db.Column(db.String())
    author_description = db.Column(db.String())
    number = db.Column(db.Integer)
    volume = db.Column(db.Integer)
    status = db.Column(db.Integer)
    created_by = db.Column(db.String())
    created_date= db.Column('created_date', db.DateTime)

    def __init__(self, category,sub_headline,article,nutshell, blurb, pullout,author,author_description,number,volume,created_by, status,headline,created_date):
        self.category = category
        self.sub_headline = sub_headline
        self.article = article
        self.nutshell = nutshell
        self.blurb = blurb
        self.pullout = pullout
        self.author = author
        self.author_description = author_description
        self.number = number
        self.volume = volume
        self.status = status
        self.created_by = created_by
        self.headline = headline
        self.created_date = created_date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'category': self.category,
            'sub_headline': self.sub_headline,
            'article':self.article,
            'nutshell':self.nutshell,
            'blurb':self.blurb,
            'pullout':self.pullout,
            'author':self.author,
            'author_description':self.author_description,
            'number':self.number,
            'volume':self.volume,
            'status':self.status,
            'created_by':self.created_by,
            'headline':self.headline,
            'created_date':self.created_date

        }