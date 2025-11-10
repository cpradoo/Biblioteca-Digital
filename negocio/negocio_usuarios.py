from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import buscar_usuario_por_id, buscar_usuario_por_correo, obtener_listado_usuarios
from modelos.usuario import Usuario
from ui.ingresar_datos import ingresar_datos_usuario, ingresar_id_usuario
from negocio.validaciones import validar_suscripcion, validar_eliminacion
from datos.eliminar_datos import eliminar_objeto
from negocio.tablas import tabla_usuarios_registrados


def registrar_usuarios():
    nombre, correo = ingresar_datos_usuario()
    if buscar_usuario_por_correo(correo):
        return print("El correo ya esta en uso.")
    else:
        nivel_suscripcion = validar_suscripcion()
    usuario_nuevo = Usuario(nombre=nombre, correo=correo, nivel_suscripcion=nivel_suscripcion)
    insertar_objeto(usuario_nuevo)


def listar_usuarios():
    if obtener_listado_usuarios():
        print("\nUsuarios Registrados:\n", tabla_usuarios_registrados())
    else:
        print("No hay usuarios registrados. ")


def actualizar_usuarios():
    try:
        usuario = buscar_usuario_por_id(ingresar_id_usuario())
        if not usuario:
            return print("Usuario no encontrado.")
        suscripcion_nueva = validar_suscripcion()
        usuario.nivel_suscripcion = suscripcion_nueva
        actualizar_objeto()
    except ValueError:
        print("ID invalida")


def eliminar_usuarios():
    usuario = buscar_usuario_por_id(ingresar_id_usuario())
    if not usuario:
        return print("Usuario no encontrado.")
    eliminar = validar_eliminacion()
    if eliminar:
        eliminar_objeto(usuario)