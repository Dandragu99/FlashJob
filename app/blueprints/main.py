'''
Aquí estaría lo que vería una persona cuanod entre a tu página web.
'''

from flask import Blueprint, render_template 

main = Blueprint('main', __name__,template_folder='--/--/templates')


@main.route('/')
def index():
    return render_template('main_base.html')

