#IMPORTANDO LAS LIBRERIAS
from flask import Flask

#IMPORTANDO PARA LA BASE DE DATOS
from extencion import db

#DEFINIMOS EL FLASK
app = Flask(__name__)
#PARA EL TOKEN DEL FORMULARIO
app.config['SECRET_KEY'] = 'secret1234'

#para la conexion con la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/db_tareas"
# initialize the app with the extension
db.init_app(app)
#para crear la tabla cuando no esta creada en la base de datos
from model import Tarea
with app.app_context():
    db.create_all()

#LLAMAMOS A LAS RUTAS
from routes import *

#ASEGURANDO QUE LA APLICACION SE EJECUTE SOLO SI SE EJECUTA DIRECTAMENTE Y NO DESDE OTRA RUTA O APLICACION
if __name__ == '__main__':
    app.run(debug = True)
    
