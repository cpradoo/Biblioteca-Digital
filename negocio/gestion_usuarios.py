from datos.conexion import sesion
from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import obtener_listado_usuarios
from modelos.usuario import Usuario
from prettytable import PrettyTable


def registrar_usuarios():
    print()
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    nivel_suscripcion = input("Suscripcion (gratuita/premium): ")
    if not nombre or not correo:
        print("Ingrese nombre y correo.")
        return
    if not nivel_suscripcion:
        nivel_suscripcion = "gratuita"
    else:
        nivel_suscripcion = nivel_suscripcion.lower()
        if nivel_suscripcion not in ["gratuita", "premium"]:
            print("Suscripcion invalida.")
            return
    usuarios = obtener_listado_usuarios()
    if usuarios:
        for usuario in usuarios:
            if usuario.correo.lower() == correo.lower():
                print("El correo ya esta en uso.")
                return
    usuario_nuevo = Usuario(nombre=nombre, correo=correo, nivel_suscripcion=nivel_suscripcion)
    insertar_objeto(usuario_nuevo)


def listar_usuarios():
    usuarios = obtener_listado_usuarios()
    tabla_usuarios = PrettyTable(["ID", "Nombre", "Correo", "Suscripcion"])
    for usuario in usuarios:
        tabla_usuarios.add_row([usuario.id, usuario.nombre, usuario.correo, usuario.nivel_suscripcion])
    print("\nUsuarios Registrados: ")
    print(tabla_usuarios)


def actualizar_usuarios():
    try:
        id_usuario = int(input("ID del usuario: "))
        suscripcion_nueva = input("Nueva suscripcion: ").lower()
        usuario = sesion.get(Usuario, id_usuario)
        if not usuario:
            print("Usuario no encontrado")
            return
        if suscripcion_nueva not in ["gratuita", "premium"]:
            print("Suscripcion invalida")
            return
        usuario.nivel_suscripcion = suscripcion_nueva
        actualizar_objeto()
    except ValueError:
        print("ID invalida")