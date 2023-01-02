class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    
    def saludo(self):
        print('Hola soy un', self.tipo, 'y me llamo', self.nombre, 'yo hago el sonido de un', self.sonido)
        
class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'
    
gato = Gato('salem', 'maullido')
gato.saludo()

perro = Perro('lobo', 'ladrido')
perro.saludo()