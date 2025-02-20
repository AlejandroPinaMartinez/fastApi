class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

class Receta:
    def __init__(self, id_receta, nombre, id_usuario):
        self.id_receta = id_receta
        self.nombre = nombre
        self.id_usuario = id_usuario

class Ingrediente:
    def __init__(self, id_ingrediente, nombre):
        self.id_ingrediente = id_ingrediente
        self.nombre = nombre
