from app import db


class ALL(db.Model):

    Description = db.Column(db.String(250), primary_key=True)
    Status = db.Column(db.String(250), index=True)
    Deadline = db.Column(db.Date)

    def __repr__(self):
        return self.Description
