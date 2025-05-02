#Crea una lista con 5 números.
#Pide un número al usuario y verifica si está en la lista usando in.

lista = [1,2,3,4,5]
numUsuario = int(input("Digita un numero para saber si esta en la lista: "))

if numUsuario in lista:
    print("El numero esta en la lista")
else :
    print("El numero no esta en la lista")
