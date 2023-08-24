#Creación y configuración del app 
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin1234@localhost:3311/flask_shopy_2687365'
    #Mensaje de seguridad para prevencion de ataques
    SECRET_KEY = "lo que se quiera aqui..."