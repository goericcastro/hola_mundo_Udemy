inombre = input('Inserta nombre:')
iapellido = input('Inserta apellido:')

def agregaNombreArchivo(nombre, apellido):
    c = open('listaNombre.txt', 'a')
    c.write(nombre + ' ' + apellido + '/n')
    c.close()

agregaNombreArchivo(inombre, iapellido)