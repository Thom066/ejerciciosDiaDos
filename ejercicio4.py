#Pide al usuario su edad.
#Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
#Si está en el rango correcto, imprime "Edad válida".

edadUsuario = int(input("Digita tu edad: "))

if edadUsuario <= 0 or edadUsuario >= 120:
    print("Edad no valida")
else :
    print("Edad valida")