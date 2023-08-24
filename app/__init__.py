from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_bootstrap import Bootstrap

#blue_print 
from .mi_blueprint import mi_blueprint
from app.productos import productos

#referencia circular from .models import Cliente,Producto,Venta,Detalle 

#Creación y configuración de la app

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)



#Registro de blue_prints
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

#Crear los objetos de SQLAlchemy y Migrate
db = SQLAlchemy(app)
migrate = Migrate(app,db)
from .models import Cliente,Producto,Venta,Detalle 

