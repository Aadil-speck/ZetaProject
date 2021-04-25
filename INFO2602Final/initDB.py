from main import app, Tutor
from models import db
import csv

db.create_all(app=app)

with open('App/tutor.csv') as tutor_file:
  tutor = csv.DictReader(tutor_file)

  for t in tutor:
      newTutor = Tutor(id=t['id'], Firstname=t['Firstname'], Lastname=t['Lastname'], Username=t['Username'], contact=t['contact'], email=t['email'], address=t['address'],Rate=t['Rate'], password=t['password'])

      if newTutor.address == "":
        newTutor.address = None
      if newTutor.id == "":
        newTutor.id = None
      if newTutor.Firstname == "":
        newTutor.Firstname = None
      if newTutor.Lastname == "":
        newTutor.Lastname = None
      if newTutor.Username == "":
        newTutor.Username = None
      if newTutor.contact == "":
        newTutor.contact = None
      if newTutor.email == "":
        newTutor.email = None
      if newTutor.address == "":
        newTutor.address = None
      if newTutor.Rate == "":
        newTutor.Rate = None
      if newTutor.password == "":
        newTutor.password = None     

      db.session.add(newTutor)
db.session.commit()
print('database initialized!')