#importando la clase para usar formularios
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#creando la clase con sus campos para el formulario
class FormAgregarTareas(FlaskForm):
    titulo = StringField('Titulo', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
class FormBuscarTareas(FlaskForm):
    buscar = StringField('Buscar', validators=[DataRequired()])
    enviar_buscar = SubmitField('Buscar')
    