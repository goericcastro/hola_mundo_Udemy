primer_numero = input("Ingrese primer numero: ")
try:
    primer_numero = int(primer_numero)
except:
    primer_numero = "chanchito feliz"

if primer_numero == "chanchito feliz":
    print("Ingresaste primer datos erroneo")
    exit()
    
segundo_numero = input("Ingrese segundo numero: ")

try:
    segundo_numero = int(segundo_numero)
except:
    segundo_numero = "chanchito feliz"

if segundo_numero == "chanchito feliz":
    print("Ingresaste segundo datos erroneo")
    exit()

if primer_numero == "chanchito feliz" or segundo_numero == "chanchito feliz":
    
 print("ingresaste mal los numeros, prueba ingresar solo numeros")
 

operador = input("Ingrese operador: ")

if operador == "+":
    print("Suma: ", primer_numero + segundo_numero)
elif operador == "-":
    print("Resta: ", primer_numero - segundo_numero)
elif operador == "*":
    print("Multiplicación: ", primer_numero * segundo_numero)
elif operador == "/":
    print("División: ", primer_numero / segundo_numero)    
    
else:
    print("El operador es invalido")