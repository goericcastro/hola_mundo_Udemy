primer_numero = input("Ingrese primer numero: ")
try:
    primer_numero = int(primer_numero)
except:
    primer_numero = "chanchito feliz"
    
segundo_numero = input("Ingrese segundo numero: ")

try:
    segundo_numero = int(segundo_numero)
except:
    segundo_numero = "chanchito feliz"

if primer_numero == "chanchito feliz" or segundo_numero == "chanchito feliz":
    
 print("ingresaste mal los numeros, prueba ingresar solo numeros")
 
else:
    print(primer_numero + segundo_numero)