from app import DB

class Producto(DB.Model): # DB.Model comvierte la clase en una tabla
    id = DB.Column(DB.Integer, primary_key = True) # Define la clase primaria
    nombre = DB.Column(DB.String(100), nullable = False) # nullable=False, Obliga a que el campo tenga valor evitando datos incompletos
    cantidad = DB.Column(DB.Integer, default = 0) # default=0 asegura que la cantidad nunca sea NULL
    precio = DB.Column(DB.Float, nullable = False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'