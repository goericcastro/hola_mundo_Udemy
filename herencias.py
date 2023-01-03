class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print('Hola!, mi nombre es:', self.nombre, self.apellido)
        
class Admin(Usuario):
    def superSaludo(self):
        print('Hola, soy administradora:', self.nombre, self.apellido)
        
usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Eric', 'Castro')
usuario3 = Usuario('bran', ' Castro')

usuario3.nombre = 'Brandon' #edita el nombre de self.nombre de usuario3
   
usuario.saludo()   
usuario2.saludo()
usuario3.saludo()
        
admin = Admin('Dhara', 'Castro')
admin.superSaludo()