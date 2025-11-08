from negocio.validaciones import validar_suscripcion


def ingresar_usuario():
    id_usuario = input("Ingrese su ID: ")
    return id_usuario


def ingresar_recurso():
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


def actualizar_suscripcion():
    id = input("Ingrese su ID: ")
    suscripcion_nueva = validar_suscripcion()
    return id,suscripcion_nueva