from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable= False)
    password = db.Column(db.String(100), nullable= False)
    rol = db.Column(db.String(100), nullable= False)
    

    # Este método se usa para representar el objeto creado más arriba. Hace algo así como print(usuario)
    def __repr__(self):
        # Aquí está devolviendo el nombre el usuario que en su defecto has llamado o llamarás en un futuro
        return f'<User {self.name}>'
    
#Crear tabla ofertas: id, título, descripción, fecha, id_contratador.
    
class Oferta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(500),nullable=False)
    fecha = db.Column(db.String(100), nullable=False)
    id_contratador = db.Column(db.Integer, nullable=False)
    # aquí tocaría hacer algo parecido a lo de arriba.
    def __repr__(self):
        return  f'Oferta {self.titulo }'




