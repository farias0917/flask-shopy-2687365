from . import productos
from flask import render_template
from .forms import newProductForm

#Crear las rutas  del blue_print
@productos.route("/crear")
def crear():
    form = newProductForm()
    return render_template("new.html", form  = form )