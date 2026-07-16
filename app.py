from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:password@localhost/Gestor_de_inventario' # SQLALCHEMY_DATABASE_URI: define la conexión a MySQL usando el driver pymysql 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactiva un sistema de seguimiento que consume memoria innecesaria


DB = SQLAlchemy(app)