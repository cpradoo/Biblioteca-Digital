from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import obtener_listado_usuarios, buscar_usuario_por_id
from modelos.usuario import Usuario
from ui.ingresar_datos import ingresar_datos_usuario, ingresar_id_usuario
from negocio.validaciones import validar_suscripcion
from datos.eliminar_datos import eliminar_objeto
from negocio.listados import tabla_usuarios_registrados


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
    tabla = tabla_usuarios_registrados()
    print(tabla)


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


def eliminar_usuario():
    usuario = buscar_usuario_por_id(ingresar_id_usuario())
    if not usuario:
        return print("Usuario no encontrado.")
    confirmacion = input("1 = Confirmar | 0 = Volver Atras: ")
    if confirmacion == "1":
        eliminar_objeto(usuario)
    elif confirmacion == "0":
        print("Cancelado.")
    else:
        print("Opcion invalida")


def eliminar_usuario():
    usuario = buscar_usuario_por_id(ingresar_id_usuario())
    if not usuario:
        return print("Usuario no encontrado.")
    while True:
        eliminar = input("1 = Confirmar | 0 = Volver Atrás: ")
        if eliminar == "1":
            eliminar_objeto(usuario)
            break
        elif eliminar == "0":
            print("Cancelado.")
            break
        else:
            print("Valor invalido, intente nuevamente.")