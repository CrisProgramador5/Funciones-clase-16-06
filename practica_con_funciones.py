lista_de_usuarios = []

def ingresar_usuario(nombre_usuario):
    lista_de_usuarios.append(nombre_usuario)
    print(lista_de_usuarios)

def eliminar_usuario(nombre_usuario):
    lista_de_usuarios.remove(nombre_usuario)

def buscar_usuario(nombre_usuario):
    for i in lista_de_usuarios:
        if(i == nombre_usuario):
            break
        else:
            return False
    return True


ingresar_usuario("Pepito")
ingresar_usuario("Alex")
ingresar_usuario("Damian")
ingresar_usuario("Joshua")

eliminar_usuario("Alex")

ingresar_usuario("Tyler")

buscar_usuario("Pepito")
buscar_usuario("Damian")


