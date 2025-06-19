print("====Bienvenido al menu de reservas====")

reservas = []

def opcion1():
    nombres = (input("Porfavor ingrese su nombre"))
    print("Reserva guardada correctamente")

def opcion2():
     print

while True:
    print("1.--Ingresar reserva--")
    print("2.--Buscar reserva--")
    print("3.--Eliminar reserva--")
    print("4.--Mostrar todas las reservas--")
    print("5.--Salir--")

    opciones = (1,2,3,4,5)

    if opciones == 1:
        opcion1()

    if opciones == 2:


    try:
        opciones = int(input("Ingrese su seleccion: "))
        if opciones < 1 or opciones > 5:
            print("Opcion no valida ingrese un numero entre 1 y 5")
    except ValueError:
            print("Opcion no valida intente otra vez")

