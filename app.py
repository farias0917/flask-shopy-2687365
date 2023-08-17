from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_bootstrap import Bootstrap

#Creación y configuración del app 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3306/flask_shopy_2687365'
#Mensaje de seguridad para prevencion de ataques
app.config["SECRET_KEY"] = "lo que se quiera aqui..."
bootstrap=Bootstrap(app)

#Crear los objetos de SQLAlchemy y Migrate
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#Modelos
class Cliente(db.Model):
    __tablename__= "clientes"
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(128))

class Producto(db.Model):
    __tablename__= "productos"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision = 10,scale =2 ))
    imagen = db.Column(db.String(100))

class Venta(db.Model):
    __tablename__= "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime,default=datetime.utcnow)
    cliente_id=db.Column(db.Integer, db.ForeignKey('clientes.id'))#La tabla en minuscula y linea para la conexion

class Detalle(db.Model):
     __tablename__= "detalles"
     id = db.Column(db.Integer, primary_key = True)
     produto_id=db.Column(db.Integer, db.ForeignKey('productos.id'))
     venta_id=db.Column(db.Integer, db.ForeignKey('ventas.id'))


#Definir el formulario de registro de productos

class NuevoProducto(FlaskForm):
    name = StringField("Nombre del producto")
    precio = StringField("Precio del producto")
    submit = SubmitField("Registrar Producto")

@app.route("/", methods=["GET","POST"])
def registrar():
    form = NuevoProducto()
    p=Producto()#llenar el objeto del producto
    if  form.validate_on_submit():
        #Registrar el producto en bd
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        return "Producto registrado"
    return render_template("registrar.html", form = form)


