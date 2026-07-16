from flask import Flask, render_template, request, redirect, url_for
import config
from extension import db
from models import Producto


app = Flask(__name__)
app.config.from_object(config) # carga la configuracion
db.init_app(app) # inicializa SQLAlchemy con la app

with app.app_context():
    db.create_all() # crea las tablas si no existen

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
    db.session.add(nuevo) # Agrega un nuevo objeto a la base
    db.session.commit() # Guarda los cambios en MySQL
    return redirect(url_for('index')) # Redirige para evitar reenvios de formularios

if __name__ == '__main__':
    app.run(debug=True)