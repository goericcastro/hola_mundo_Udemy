lista = [3, 5, 56, 3, 2]
menor = 'init'
for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor
        
print('menor', menor) 