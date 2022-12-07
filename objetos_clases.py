class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
usuario = Usuario("Alberto", "Feliz")
usuario2 = Usuario("Chanchito", "Feliz")

print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)
        
    