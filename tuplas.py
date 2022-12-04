tupla = ("hola", "mundo", "somos","tupla"), 5
#print(tupla.count("tupla"))
#print(tupla.index(1)) # identifica en que columna esta el elemento


#tupla.append() #no funciona en tuplas
#convertir_lista_a_tupla = list(tupla)
#convertir_lista_a_tupla.append(4)
#print(convertir_lista_a_tupla)

#rango = range(6)
#print(rango)

diccionario ={
    "nombre": "Salem",
    "raza": "Bombei Americano",
    "edad": 5
}
#print(diccionario) 

#print(diccionario["raza"]) # obtener valores de dicionario

#print(diccionario.get("nombre")) # obtener valores de dicionario otro metodo
diccionario["nombre"] = "Fluffy"

#print(diccionario)

#print(len(diccionario))

#diccionario["ronronea"] = "si" # Agrega mas valores al diccionario

#print(diccionario)

#diccionario.pop("ronronea") # Borra Valor agregado

#diccionario.popitem() # Borra ultimo valor agregado

#del diccionario["ronronea"]

#print(diccionario)

gatitos = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4,
        "raza": "Mumbei Americano"
     },
    "Salem": {
        "nombre": "Salem",
        "edad": 6,
        "raza": "preto"
    }
}
print(gatitos)

