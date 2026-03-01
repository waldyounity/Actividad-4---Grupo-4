#IMPORTAMOS RENDER TEMPLATE
from flask import render_template, redirect, url_for  # ← AÑADIDO redirect y url_for

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
    
    if formulario.validate_on_submit():
        nueva_tarea = Tarea(titulo = formulario.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit() 
        print('Se envio correctamente', formulario.titulo.data)
        # CAMBIADO: Redirigir para evitar reenvío del formulario
        return redirect(url_for('nosotros'))
    
    # NUEVO: Obtener todas las tareas para mostrarlas
    tareas = Tarea.query.all()
    # MODIFICADO: Enviar tareas al template
    return render_template('nosotros.html', form=formulario, tareas=tareas)

@app.route('/saludo')
def saludo():
    return 'Hola bienvenido a Taller Apps'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola {nombre} bienvenido a Taller Apps'


# Ruta para mostrar una tarea específica (MANTENERLA para ver detalles)
@app.route('/tarea/<int:id>')
def mostrar_tarea(id):
    tarea = Tarea.query.get_or_404(id)
    return render_template('mostrar_tarea.html', tarea=tarea)

# NUEVA RUTA PARA ELIMINAR TAREAS
@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    tarea_a_eliminar = Tarea.query.get_or_404(id)
    db.session.delete(tarea_a_eliminar)
    db.session.commit()
    return redirect(url_for('nosotros'))