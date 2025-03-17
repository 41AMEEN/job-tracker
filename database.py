from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pending")
    applied_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<JobApplication {self.company} - {self.title}>"
 
