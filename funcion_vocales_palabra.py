palabra = input()
vocales = 0

for x in palabra:
    vocales += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0
print(vocales)

#2do método con funcion

def pala(voc):
    return voc == voc + 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0

resultado = pala(palabra)
print(resultado)