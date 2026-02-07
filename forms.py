from wtforms import Form
from wtforms import StringField, EmailField, IntegerField, RadioField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula",[
        validators.DataRequired(message="El campo es requerido")
    ])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido=StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido")
    ])

class CinepolisForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El nombre es obligatorio')
    ])
    compradores = IntegerField('Cantidad Compradores', [
        validators.DataRequired(message='Ingrese número de compradores'),
        validators.NumberRange(min=1, message='Mínimo 1 comprador')
    ])
    boletas = IntegerField('Cantidad De Boletas', [
        validators.DataRequired(message='Ingrese cantidad de boletas'),
        validators.NumberRange(min=1, message='Mínimo 1 boleta')
    ])
    cineco = RadioField('Tarjeta Cineco', 
                        choices=[('si', 'Sí'), ('no', 'No')], 
                        default='no')