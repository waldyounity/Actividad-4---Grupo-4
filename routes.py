#IMPORTAMOS RENDER TEMPLATE
from flask import render_template

#IMPORTANDO LA APLICACION
from app import app, db

#IMPORTANDO PARA USAR FORMULARIOS
import formularios
#importando el modelo
from model import Tarea

from flask import request, redirect

#CREAMOS LA RUTA CON LA FUNCION QUE DEVUELVE
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', subtitulo = 'Actividad en grupo TAI')

@app.route('/nosotros', methods = ['GET', 'POST'])
def nosotros():
    formulario = formularios.FormAgregarTareas()
    buscar_formulario = formularios.FormBuscarTareas()
    resultados = [] # Aquí guardaremos lo que encontremos

    # LÓGICA PARA AGREGAR TAREA
    if formulario.validate_on_submit() and 'enviar' in request.form:
        nueva_tarea = Tarea(titulo=formulario.titulo.data)
        db.session.add(nueva_tarea)
        db.session.commit()
        return redirect('/nosotros')

    # LÓGICA PARA BUSCAR TAREA
    if buscar_formulario.validate_on_submit() and 'enviar_buscar' in request.form:
        termino = buscar_formulario.buscar.data
        # Buscamos coincidencias parciales (LIKE)
        resultados = Tarea.query.filter(Tarea.titulo.contains(termino)).all()

    return render_template('nosotros.html',form=formulario,buscarform=buscar_formulario,resultados=resultados)


@app.route('/saludo')
def saludo():
    return 'Hola bienvenido a Taller Apps'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola {nombre} bienvenido a Taller Apps'