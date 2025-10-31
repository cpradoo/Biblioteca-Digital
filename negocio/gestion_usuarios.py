from datos.conexion import sesion
from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import obtener_listado_usuarios
from modelos.usuario import Usuario
from prettytable import PrettyTable


def registrar_usuarios():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    nivel_suscripcion = input("Suscripcion (gratuita/premium): ")
    if not nombre or not correo:
        print("Ingrese nombre y correo.")
        return
    if not nivel_suscripcion:
        nivel_suscripcion = "gratuita"
    else:
        nivel_suscripcion = nivel_suscripcion.lower().strip()
        if nivel_suscripcion not in ["gratuita", "premium"]:
            print("Suscripcion invalida.")
            return
    usuarios = obtener_listado_usuarios()
    if usuarios:
        for usuario in usuarios:
            if usuario.correo.lower().strip() == correo.lower().strip():
                print("El correo ya esta en uso.")
                return
    nuevo_usuario = Usuario(nombre=nombre, correo=correo, nivel_suscripcion=nivel_suscripcion)
    insertar_objeto(nuevo_usuario)


def listar_usuarios():
    usuarios = obtener_listado_usuarios()
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ["ID", "Nombre", "Correo", "Suscripción"]
    for usuario in usuarios:
        tabla_usuarios.add_row([usuario.id, usuario.nombre, usuario.correo, usuario.nivel_suscripcion])
    print("\n========================= Usuarios Registrados =========================")
    print(tabla_usuarios)


def actualizar_usuarios():
    try:
        id_usuario = int(input("ID del usuario: "))
        cambiar_suscripcion = input("Nueva suscripcion: ").strip().lower()
        usuario = sesion.query(Usuario).filter_by(id=id_usuario).first()
        if not usuario:
            print("Usuario no encontrado")
            return
        if cambiar_suscripcion not in ["gratuita", "premium"]:
            print("Suscripcion invalida")
            return
        usuario.nivel_suscripcion = cambiar_suscripcion
        actualizar_objeto()
    except ValueError:
        print("ID invalida")