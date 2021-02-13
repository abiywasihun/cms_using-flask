from cms import db

class StoryProposal(db.Model):
    __tablename__ = 'StoryProposal'
     
    id = db.Column(db.Integer, primary_key=True)
    reporter = db.Column(db.String())
    number = db.Column(db.Integer)
    initialHeadline = db.Column(db.String())
    possibleIssues = db.Column(db.String())
    initialLead = db.Column(db.String())
    contextOfStory = db.Column(db.String())
    institutionsToVisit = db.Column(db.String())
    listOfMaterial = db.Column(db.String())
    listOfPeople = db.Column(db.String())
    listOfExpert = db.Column(db.String())
    nameOfExpert = db.Column(db.String())
    suggestionMedia = db.Column(db.String())
    section = db.Column(db.String())
    draftID = db.Column(db.Integer)
    status = db.Column(db.Integer)
    updated_at= db.Column('updated_at', db.DateTime)

    def __init__(self, reporter,number,initialHeadline,possibleIssues, initialLead, contextOfStory,
                         institutionsToVisit,listOfMaterial,listOfPeople,listOfExpert,nameOfExpert, 
                         suggestionMedia,section, draftID,status, updated_at):
        self.reporter = reporter
        self.number = number
        self.initialHeadline = initialHeadline
        self.possibleIssues = possibleIssues
        self.initialLead = initialLead
        self.contextOfStory = contextOfStory
        self.institutionsToVisit = institutionsToVisit
        self.listOfMaterial = listOfMaterial
        self.listOfPeople = listOfPeople
        self.listOfExpert = listOfExpert
        self.nameOfExpert = nameOfExpert
        self.suggestionMedia = suggestionMedia
        self.section = section
        self.draftID = draftID
        self.status = status
        self.updated_at = updated_at

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'reporter': self.reporter,
            'number': self.number,
            'initialHeadline':self.initialHeadline,
            'possibleIssues':self.possibleIssues,
            'initialLead':self.initialLead,
            'contextOfStory':self.contextOfStory,
            'institutionsToVisit':self.institutionsToVisit,
            'listOfMaterial':self.listOfMaterial,
            'listOfPeople':self.listOfPeople,
            'listOfExpert':self.listOfExpert,
            'nameOfExpert':self.nameOfExpert,
            'suggestionMedia':self.suggestionMedia,
            'section':self.section,
            'draftID':self.draftID,
            'status':self.status,
            'updated_at':self.updated_at
        }