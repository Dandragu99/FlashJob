'''
Aquí entraría el login el sign in o cualquier cosa de autorización
'''

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/user/<username>')
def profile(username):
    return render_template ('profile.html', username= username)