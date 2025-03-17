from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db, JobApplication

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobs.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

    # Add sample job applications
    sample_jobs = [
        JobApplication(company="Google", title="Software Engineer", status="Pending"),
        JobApplication(company="Microsoft", title="Backend Developer", status="Interview"),
        JobApplication(company="Amazon", title="Data Scientist", status="Applied")
    ]

    db.session.bulk_save_objects(sample_jobs)
    db.session.commit()

    print("✅ Database initialized successfully with sample job applications!")
 
