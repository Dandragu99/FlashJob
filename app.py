'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, esta es mi primera app de Flask!"

if __name__ == '__main__':
    app.run(debug=True)



'''
# El método render_template nos permite devolver una plantilla de HTML



from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


