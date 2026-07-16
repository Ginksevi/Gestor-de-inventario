from extension import db

class Producto(db.Model): # db.Model comvierte la clase en una tabla
    id = db.Column(db.Integer, primary_key = True) # Define la clase primaria
    nombre = db.Column(db.String(100), nullable = False) # nullable=False, Obliga a que el campo tenga valor evitando datos incompletos
    cantidad = db.Column(db.Integer, default = 0) # default=0 asegura que la cantidad nunca sea NULL
    precio = db.Column(db.Float, nullable = False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'