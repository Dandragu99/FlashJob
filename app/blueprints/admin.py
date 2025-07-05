'''
Aquí irían todas las funciones de administrador.
'''

from flask import Blueprint, render_template
from app.models import User
from app import db

admin = Blueprint('admin',__name__)

@admin.route('/admin')
def dashboard():
    users = User.query.all() #Obtiene todos los usuarios
    return render_template('register.html', users=users)

'''
Recuerda que esto es un una plantilla pero no define rutas.
Para ello es necesario activar esas rutas.
Cuando flask ve el @admin registra la ruta. 
'''