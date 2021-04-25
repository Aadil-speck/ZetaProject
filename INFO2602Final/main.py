import json
from flask_cors import CORS
from flask import Flask, request, jsonify, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError
from datetime import timedelta

from models import db, Logs, Tutor  #add application models
''' Begin boilerplate code '''


def create_app():
    app = Flask(__name__, static_url_path='')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = "MYSECRET"
    CORS(app)
    db.init_app(app)
    return app


app = create_app()

app.app_context().push()
''' End Boilerplate Code '''


@app.route('/')
def index():
    logs = Logs.query.all()
    return render_template('app.html', logs=logs)


@app.route('/app')
def client_app():
    return app.send_static_file('app.html')


@app.route('/logs', methods=['POST'])
def my_form():
    data = request.form
    log = Logs(stream=data['stream'], studentId=data['studentId'])
    db.session.add(log)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/logs/<id>', methods=['PUT'])
def update_log(id):
    data = request.form
    log = Logs.query.get(id)
    log.stream = data['stream']
    log.studentId = data['studentId']
    db.session.add(log)
    db.session.commit()
    return 'Updated!', 201


@app.route('/logs', methods=['GET'])
def get_logs():
    logs = Logs.query.all()
    logs = [log.toDict() for log in logs]
    return jsonify(logs)


@app.route('/updateLog', methods=['POST'])
def update_action():
    data = request.form
    log = Logs.query.get(data['id'])
    log.stream = data['stream']
    log.studentId = data['studentId']
    db.session.add(log)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/deleteLog/<id>', methods=['GET'])
def delete_action(id):
    log = Logs.query.get(id)
    db.session.delete(log)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/updateForm/<id>', methods=['GET'])
def update_form(id):
    return render_template('update.html', id=id)


@app.route('/getStats', methods=['GET'])
def get_stats():
    logs = Logs.query.all()
    count = [0, 0, 0]

    for log in logs:
        if log.stream == 1:
            count[0] += 1
        elif log.stream == 2:
            count[1] += 1
        elif log.stream == 3:
            count[2] += 1

    return jsonify([{"data": count}])


@app.route('/')
def index2():
    tutor = Tutor.query.all()
    return render_template('app.html', tutor=tutor)


@app.route('/tutor', methods=['POST'])
def my_form2():
    data = request.form
    tutor = Tutor(stream=data['stream'],
                  id=data['id'],
                  Firstname=data['Firstname'],
                  contact=data['contact'],
                  email=data['email'],
                  address=data['address'],
                  Rate=data['Rate'])
    db.session.add(tutor)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/tutor/<id>', methods=['PUT'])
def update_tutor(id):
    data = request.form
    t = Tutor.query.get(id)
    t.stream = data['stream']
    t.id = data['id']
    db.session.add(t)
    db.session.commit()
    return 'Updated!', 201


@app.route('/tutor', methods=['GET'])
def get_tutor():
    tutor = Tutor.query.all()
    tutor = [t.toDict() for t in tutor]
    return jsonify(tutor)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
