edad = int(input())

if edad >= 18:
    print('Su edad es:', edad, 'años de edad, entonces es mayor de edad')

else:
    print('Su edad es:', edad, 'alos de edad, entonces es menor de edad')
    
#2do Método con función

def esMayor(usuario):
    return usuario.edad > 18

class Usuario:
    def __init__(self, edad):
        self.edad = edad
        
usuario = Usuario(edad)

resultado = esMayor(usuario)

if resultado == True:
    print('Segundo Método, su edad es:', edad, 'años de edad, entonces es mayor de edad')
else:
    print('Segundo Método, su edad es:', edad, 'alos de edad, entonces es menor de edad')