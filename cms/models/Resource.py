from cms import db

class Resource(db.Model):
    __tablename__ = 'Resource'
     
    id = db.Column(db.Integer, primary_key=True)
    postID = db.Column(db.String())
    postType = db.Column(db.String())
    number = db.Column(db.String())
    photoCaption = db.Column(db.String())
    file = db.Column(db.String())
    filePath = db.Column(db.String())
    provider = db.Column(db.String())
    captionUpdate = db.Column(db.String())

    def __init__(self, postID,postType,number,photoCaption, file, filePath, provider, captionUpdate):
        self.postID = postID
        self.postType = postType
        self.number = number
        self.photoCaption = photoCaption
        self.file = file
        self.filePath = filePath
        self.provider = provider
        self.captionUpdate = captionUpdate

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'postID': self.postID,
            'postType': self.postType,
            'number':self.number,
            'photoCaption':self.photoCaption,
            'file':self.file,
            'filePath':self.filePath,
            'provider':self.provider,
            'captionUpdate':self.captionUpdate
        }