list = []
print('Ingrese numeros y para salir ingrese basta')

while True:
    valor = input('Ingrese numeros: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            list.append(valor)
        except:
            print('Dato Invalido')
            exit()

resultado = 0
for x in list:
    resultado = x + 1

print(resultado)