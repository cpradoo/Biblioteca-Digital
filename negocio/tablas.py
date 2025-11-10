from prettytable import PrettyTable
from datos.obtener_datos import obtener_listado_recursos, obtener_listado_usuarios, obtener_historial


def tabla_recursos_digitales():
    recursos = obtener_listado_recursos()
    tabla_recursos = PrettyTable(["ID", "Titulo", "Tipo", "Suscripcion"])
    for recurso in recursos:
        tabla_recursos.add_row([recurso.id, recurso.titulo, recurso.tipo, recurso.nivel_suscripcion])
    return tabla_recursos


def tabla_usuarios_registrados():
    usuarios = obtener_listado_usuarios()
    tabla_usuarios = PrettyTable(["ID", "Nombre", "Correo", "Suscripcion"])
    for usuario in usuarios:
        tabla_usuarios.add_row([usuario.id, usuario.nombre, usuario.correo, usuario.nivel_suscripcion])
    return tabla_usuarios


def tabla_historial_descargas():
    historial = obtener_historial()
    tabla_historial = PrettyTable(["Usuario", "Recurso Digital", "Fecha"])
    for descarga in historial:
        tabla_historial.add_row([descarga.usuario.nombre, descarga.recurso.titulo, descarga.fecha.strftime("%d/%m/%Y")])
    return tabla_historial