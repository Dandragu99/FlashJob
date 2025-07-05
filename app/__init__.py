from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creamos la instancia de SQLAlchemy
db = SQLAlchemy()

'''Crearemos una función que cree una aplicación
    y la inicializamos o la llamamos en el app.py
'''
def create_app():

    # Escpecifica la carpeta de templates
    app = Flask(__name__, template_folder='templates')

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos
    db.init_app(app)

    # Aquí importamos desde la clase models
    from app import models

    # importamos desde la clase main.py que está en blueprints lo mismo que hemos hecho más abajo
    # Todo esto también se puede hacer en la app.py




    from app.blueprints.main import main
    app.register_blueprint(main)
    
    '''Lo creado en blueprints(admin) lo podemos importar aquí, así de fácil'''
    from app.blueprints.admin import admin
    app.register_blueprint(admin)

    from app.blueprints.auth import auth
    app.register_blueprint(auth)

    from app.blueprints.api import api
    app.register_blueprint(api)


    with app.app_context():
        db.create_all()


    return app
'''
Normalmente se usa @route, pero en este caso vamos a utilizar los blueprints que es más p
profesional.
'''
