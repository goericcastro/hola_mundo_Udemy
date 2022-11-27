#Acá va un comentario
if 3 > 5:
    print("5 es mayor a 3")

#Acá va un comentario
#if 5 > 3: #Acá va otro comentario
 #   print("5 es mayor a 3")

x = 5
y = "chanchito feliz"

#print(x, y)

email = "eric.castro.ingenieria@gmail.com"

#print(email)

inicio =  "Hola "
final = "mundo"
#print(inicio + final)

palabra = "hola mundo"
oracion = "hola mundo con comilla doble"

entero = 20 #integer
conDecimales = 20.2 #float
complejo = 1j
#print(palabra, oracion, entero, conDecimales, complejo)

lista = [1, 2, 2, 5]
lista2 = lista.copy()
lista.append(4)
#print(lista)

#limpia la lista

lista2 = lista.copy()

#print(lista, lista2.count(2))

#print(lista, lista2, len(lista))

#print(len(lista), len(lista2))

count_list = len(lista)
count_list2 = len(lista2)

#print(count_list, count_list2)
#print(lista[0], lista2[3]) #busca una columna en la lista

#lista.pop() #borra datos de la lista
lista.remove(2)
print(lista)
