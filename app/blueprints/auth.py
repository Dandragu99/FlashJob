'''
Aquí entraría el login el sign in o cualquier cosa de autorización
'''

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/user/<username>')
def profile(username):
    return render_template (f'Hello,{username}')