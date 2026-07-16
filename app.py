from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Producto, DB


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:password@localhost/Gestor_de_inventario' # SQLALCHEMY_DATABASE_URI: define la conexión a MySQL usando el driver pymysql 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactiva un sistema de seguimiento que consume memoria innecesaria

DB = SQLAlchemy(app)

@app.route('/')
def index():
    productos = Producto.query.all() # query.all() es mas seguro que escribir SELECT * FROM producto manualmente, se encarga de traducir la consulta a SQL protegiendo contra inyecciones
    return render_template('index.html', productos = productos) # Busca el archivo index.html en la carpeta templates, renderiza el html platillas de jinja2 y permite pasar variables

@app.route('/agregar', methods = ['POST'])
def agregar():
    nombre = request.form['nombre'] # request.form obtiene datos del formulario html
    cantidad = int(request.form['cantidad']) # request.form obtiene datos del formulario html
    precio = float(request.form['precio']) # request.form obtiene datos del formulario html

    nuevo = Producto(nombre = nombre, cantidad = cantidad, precio = precio)
    DB.session.add(nuevo) # Agrega un nuevo objeto a la base
    DB.session.commit() # Guarda los cambios en MySQL
    return redirect(url_for('index')) # Redirige para evitar reenvios de formularios

if __name__ == '__main__':
    app.run(debug=True)