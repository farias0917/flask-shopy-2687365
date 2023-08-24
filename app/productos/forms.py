from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField

class newProductForm(FlaskForm):
    name = StringField("Ingrese el producto:")
    precio =  StringField("Ingrese precio:")
    Submit = SubmitField("Registrar")