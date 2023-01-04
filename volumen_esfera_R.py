import math

radio = int(input())

volumen_esfera = 4 / 3 * math.pi * radio ** 3

print(volumen_esfera)

#Cálculo con función
def volumen_esfera2(r):

    return 4 / 3 * math.pi * r ** 3

resultado = volumen_esfera2(radio)
print(resultado)