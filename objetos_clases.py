class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def saludo(self):
        print('Hola, mi nombre es señor:', self.nombre, self.apellido)
        
    def saludo1(self):
        print('Hola, mi nombre es señorita:', self.nombre, self.apellido)
        

usuario = Usuario('Eric', 'Castro')
usuario2 = Usuario('bran', 'Ticona')
usuario3 = Usuario('dhara', 'Castro')

usuario.saludo()
usuario2.saludo()
usuario3.saludo1()
        
        