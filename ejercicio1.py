#Pide tres números al usuario.
#Usa condicionales (if) para decir cuál es el más pequeño.

numero1 = int(input("Digita el primer numero: "))
numero2 = int(input("Digita el segundo numero: "))
numero3 = int(input("Digita el tercer numero: "))

if numero1 < numero2 and numero1 < numero3:
    print("El numero menor es:",numero1)
elif numero2 < numero1 and numero2 < numero3:
    print("El numero menor es:",numero2)
else :
    print("El numero menor es:",numero3)

