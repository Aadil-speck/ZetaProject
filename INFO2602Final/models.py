from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()
import datetime


class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId =  db.Column(db.Integer, nullable=False)
    stream = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def toDict(self):
        return{
            'id': self.id,
            'studentId': self.studentId,
            'stream': self.stream,
            'created': self.created.strftime("%m/%d/%Y, %H:%M:%S")
        }

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.String(80), unique=True, nullable=False)
    Lastname = db.Column(db.String(80), unique=True, nullable=False)
    Username = db.Column(db.String(80), unique=True, nullable=False)
    contact = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    Rate = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
      return {
          "id": self.id,
          "Firstname": self.Firstname,
          "Lastname": self.Lastname,
          "contact": self.contact,
          "email": self.email,
          "address": self.address,
          "Rate": self.Rate,
          "password":self.password
      }
    
    #hashes the password parameter and stores it in the object
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    #Returns true if the parameter is equal to the object's password property
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    #To String method
    def __repr__(self):
        return '<Tutor {}>'.format(self.Firstname, self.Lastname)  

class Courses(db.Model):
    Course_Id = db.Column(db.Integer, primary_key=True)
    Course_name = db.Column(db.String(80), unique=True, nullable=False)
    Description = db.Column(db.String(120), unique=True, nullable=False)

    def toDict(self):
        return {
            "Course_Id" : self.Course_Id,
            "Course_name": self.Course_name,
            "Description": self.Description
        }

class Sessions(db.Model):
    Session_ID = db.Column(db.Integer, primary_key=True)
    tutorid = db.Column(db.Integer, db.ForeignKey('tutor.id'), nullable=False)
    courseid = db.Column(db.Integer, db.ForeignKey('courses.Course_ID'), nullable=False)
    start = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    end = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    Date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    Location = db.Column(db.String(20), unique=True, nullable=False)

    def toDict(self):
      return{
          "Session_ID" : self.Session_ID,
          "tutorid" : self.tutorid,
          "courseid" : self.courseid,
          "start" : self.start,
          "end" : self.end,
          "Date" : self.Date,
          "Location" : self.Location
      } 