from cms import db

class MyTask(db.Model):
    __tablename__ = 'myTask'
     
    id = db.Column(db.Integer, primary_key=True)
    taskTitle = db.Column(db.String())
    instruction = db.Column(db.String())
    dueDate = db.Column(db.String())
    volume = db.Column(db.Integer)
    number = db.Column(db.Integer)
    assignedTo = db.Column(db.Integer)
    assigneeID = db.Column(db.Integer)
    status = db.Column(db.Integer)


    def __init__(self, taskTitle,instruction,dueDate,volume, number, assignedTo, assigneeID, status):
        self.taskTitle = taskTitle
        self.instruction = instruction
        self.dueDate = dueDate
        self.volume = volume
        self.number = number
        self.assignedTo = assignedTo
        self.assigneeID = assigneeID
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'taskTitle': self.taskTitle,
            'instruction': self.instruction,
            'dueDate':self.dueDate,
            'volume':self.volume,
            'number':self.number,
            'assignedTo':self.assignedTo,
            'assigneeID':self.assigneeID,
            'status':self.status
        }