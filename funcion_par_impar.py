numero = int(input())

def par(num):
    return num % 2 == 0

resultado = par(numero)

if resultado == True:
    print('El resultado es PAR')
else:
    print('El resultado es IMPAR')