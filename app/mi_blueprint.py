from flask import Blueprint #Modulos

#Crear y configurar el blueprint

mi_blueprint = Blueprint("mi_blueprint", __name__, url_prefix="/ejemplo")

#Crear ruta de ejemplo para blue_print
@mi_blueprint.route("/saludo")
def saludo():
    return "<h1>LA RE GOOD PA LOS GOODS👌</h1>"



