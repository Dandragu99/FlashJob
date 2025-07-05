# Aquí se crea la api el camarero que decía mi profe

'''
Es donde se envían y se reciven los datos
'''

# Primero creamos los imports

from flask import Blueprint,request,jsonify
from app import db
from app.models import User

'''
*Recuerda*
El blueprint es el que crea el grupo de rutas
El request sirve para obtener los datos que manda el usuario
El jsonify es el que convierte los datos de PYTHON a JSON
El db para hablar con la base de datos
El User es el modelo del usuario
'''

# Segundo se crea el bluprint "como en casi todos los lados de este Flaskyecto"
api = Blueprint('api', __name__)

# Tercero la ruta, que es muy importante
@api.route('/api/adduser', methods=['GET', 'POST'])

# Cuarto, obtenemos los datos, importantísimo también 
def add_user():
    try:
        name = request.args.get('name')
        email = request.args.get('email')
        rol = request.args.get('vendedor')
        password = request.args.get('contraseña')
        '''
        Esto es lo que sirve para tomar los parámetros de la URL
        /api/adduser?name=Juan&email=juan@gmail.com
        '''
# Quinto, lo validamos
        if not all ([name, email, password,rol]):
            return jsonify({'error': 'Faltan campos'}), 400
        '''
        En esta parte validamos los campos para que estén presentes
        '''
# Sexto paso, cremos el usuario
        user = User(name = name, email = email, password = password, rol = rol)
        db.session.add(user)
        db.session.commit
        '''
        El paso seis es el que crea el usuario, lo añade a la base de datos
        y lo guarda.
        '''
# Paso 7 la respuesta
        return jsonify({
            'success': True,
            'message': f'Usuario {name} creado',
            'user_id': user.id
        })

        '''
        Devuelve una respuesta en forma json
        '''

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@api.route('/api/getusers', methods =['GET'])
def get_users():
    ''' Obtiene todos los usuarios '''
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'name': u.name,
        'email': u.email,
        'rol': u.rol        
    } for u in users])