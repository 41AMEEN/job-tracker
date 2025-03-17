from flask import Flask, render_template, request, redirect, url_for
from database import db, JobApplication

app = Flask(__name__)  # Create Flask application
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobs.db"  # Connect to SQLite database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disable modification tracking
db.init_app(app)  # Initialize database with Flask

# Home page - Show all job applications
@app.route("/")
def index():
    jobs = JobApplication.query.all()  # Fetch all job applications
    return render_template("index.html", jobs=jobs)

# Add new job application
@app.route("/add", methods=["POST"])
def add_job():
    company = request.form["company"]
    title = request.form["title"]
    new_job = JobApplication(company=company, title=title, status="Applied")
    db.session.add(new_job)
    db.session.commit()
    return redirect(url_for("index"))

# Update job application status
@app.route("/update/<int:job_id>", methods=["POST"])
def update_job(job_id):
    job = JobApplication.query.get(job_id)
    if job:
        job.status = request.form["status"]
        db.session.commit()
    return redirect(url_for("index"))

# Delete job application
@app.route("/delete/<int:job_id>")
def delete_job(job_id):
    job = JobApplication.query.get(job_id)
    if job:
        db.session.delete(job)
        db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure database tables exist
    app.run(debug=True)

