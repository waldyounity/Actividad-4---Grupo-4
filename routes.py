#IMPORTAMOS RENDER TEMPLATE
from flask import render_template

#IMPORTANDO LA APLICACION
from app import app, db

#IMPORTANDO PARA USAR FORMULARIOS
import formularios
#importando el modelo
from model import Tarea


#CREAMOS LA RUTA CON LA FUNCION QUE DEVUELVE
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', subtitulo = 'Actividad en grupo TAI')

@app.route('/nosotros', methods = ['GET', 'POST'])
def nosotros():
    formulario = formularios.FormAgregarTareas()
    if formulario.validate_on_submit() :
        nueva_tarea = Tarea(titulo = formulario.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit() 
        print('Se envio correctamente', formulario.titulo.data)
        return render_template('nosotros.html', form = formulario, titulo = formulario.titulo.data)
    return render_template('nosotros.html', form = formulario)

@app.route('/saludo')
def saludo():
    return 'Hola bienvenido a Taller Apps'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola {nombre} bienvenido a Taller Apps'

# Ruta para mostrar todas las tareas
@app.route('/tareas')
def listar_tareas():
    tareas = Tarea.query.all()
    return render_template('tareas.html', tareas=tareas)

# Ruta para mostrar una tarea específica
@app.route('/tarea/<int:id>')
def mostrar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    return render_template('mostrar_tarea.html', tarea=tarea)