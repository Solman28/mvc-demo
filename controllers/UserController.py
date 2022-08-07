# pseudo code
from flask import render_template, redirect, url_for, request, abort, flash
from models.User import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    users = User.query.all()
    return render_template('user/index_user.j2', users=users)

def store():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['address'] or not request.form['age']:
            flash('Por favor ingresa todos los campos', 'error')
        else:
            name = request.values.get('name') 
            email = request.values.get('email') 
            address = request.values.get('address') 
            age = request.values.get('age') 

            objUser = User()
            objUser.name = name
            objUser.email = email
            objUser.address = address
            objUser.age = age

            db.session.add(objUser)
            db.session.commit()

            flash('Usuario registrado correctamente!', 'info')

        return render_template('user/create_user.j2')
    
    return render_template('user/create_user.j2')

def show(userId):
    ...

def update(userId):
    ...

def delete(userId):
    ...
