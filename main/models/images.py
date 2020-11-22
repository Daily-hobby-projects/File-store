
from ..extensions.database import db
from datetime import datetime


class Image(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    filename=db.Column(db.String(255),nullable=False)
    file_path=db.Column(db.String(255),nullable=False)
    description=db.Column(db.Text())
    date_added=db.Column(db.DateTime(),default=datetime.utcnow)

    def __init__(self,filename,file_path,description,date_added):
        self.filename=filename
        self.file_path=file_path
        self.description=description
        self.date_added=date_added

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"{self.filename} uploaded {self.date_added}"