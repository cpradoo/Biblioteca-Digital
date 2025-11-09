def ingresar_id_usuario():
    id_usuario = input("Ingrese su ID: ")
    return id_usuario


def ingresar_id_recurso():
    id_recurso = input("Ingrese la ID del recurso: ")
    return id_recurso


def ingresar_datos_recurso():
    print()
    titulo = input("Titulo: ")
    tipo = input("Tipo: ")
    return titulo, tipo


def ingresar_datos_usuario():
    print()
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    return nombre, correo