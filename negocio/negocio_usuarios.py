from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import obtener_listado_usuarios, buscar_usuario_por_id
from modelos.usuario import Usuario
from prettytable import PrettyTable
from ui.ingresar_datos import ingresar_datos_usuario, ingresar_usuario
from negocio.validaciones import validar_suscripcion


def registrar_usuarios():
    nombre, correo = ingresar_datos_usuario()
    nivel_suscripcion = validar_suscripcion()
    usuarios = obtener_listado_usuarios()
    if usuarios:
        for usuario in usuarios:
            if usuario.correo.lower() == correo.lower():
                return print("El correo ya esta en uso.")
    usuario_nuevo = Usuario(nombre=nombre, correo=correo, nivel_suscripcion=nivel_suscripcion)
    insertar_objeto(usuario_nuevo)


def listar_usuarios():
    usuarios = obtener_listado_usuarios()
    tabla_usuarios = PrettyTable(["ID", "Nombre", "Correo", "Suscripcion"])
    for usuario in usuarios:
        tabla_usuarios.add_row([usuario.id, usuario.nombre, usuario.correo, usuario.nivel_suscripcion])
    print(tabla_usuarios)


def actualizar_usuarios():
    try:
        id_usuario = ingresar_usuario()
        usuario = buscar_usuario_por_id(id_usuario)
        if not usuario:
            return print("Usuario no encontrado.")
        suscripcion_nueva = validar_suscripcion()
        usuario.nivel_suscripcion = suscripcion_nueva
        actualizar_objeto()
    except ValueError:
        print("ID invalida")


def eliminar_usuario():
    pass