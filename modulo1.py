import modulos
from camelcase import CamelCase

c = CamelCase()
s = 'esta oración necesita camelcase'

print(c.hump(s))

print(modulos.mascotas)
    
modulos.saludo('Nicolas')