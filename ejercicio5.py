#Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#Pide al usuario su nombre.
#Usa if para decir si está en la lista de invitados o no.

nombres = ['ana', 'luis', 'sofia']
nombreUsuario = str(input("Digita tu nombre: ")).lower()

if nombreUsuario in nombres:
    print("Estas en la lista de invitados")
else :
    print("No estas en la lista de invitados")