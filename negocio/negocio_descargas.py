from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_listado_recursos, obtener_historial, buscar_usuario_por_id, buscar_recurso_por_id
from modelos.historial import HistorialDescargas
from prettytable import PrettyTable
from datetime import datetime
from ui.ingresar_datos import ingresar_usuario, ingresar_recurso


def descargar_recurso():
    try:
        id_usuario = ingresar_usuario()
        usuario = buscar_usuario_por_id(id_usuario)
        if not usuario:
            return print("Usuario no encontrado.")
        recursos = obtener_listado_recursos()
        tabla_recursos = PrettyTable(["ID", "Titulo", "Tipo", "Suscripcion"])
        for recurso in recursos:
            tabla_recursos.add_row([recurso.id, recurso.titulo, recurso.tipo, recurso.nivel_suscripcion])
        id_recurso = ingresar_recurso()
        recurso = buscar_recurso_por_id(id_recurso)
        if not recurso:
            return print("Recurso no encontrado.")
        if recurso.nivel_suscripcion == "premium" and usuario.nivel_suscripcion != "premium":
            return print("Necesita suscripcion premium.")
        descarga_nueva = HistorialDescargas(id_usuario=usuario.id,id_recurso=recurso.id,fecha=datetime.now())
        insertar_objeto(descarga_nueva)
    except ValueError:
        print("ID invalida")


def listar_historial():
    historial = obtener_historial()
    tabla_historial = PrettyTable(["Usuario", "Recurso Digital", "Fecha"])
    for descarga in historial:
        tabla_historial.add_row([descarga.usuario.nombre, descarga.recurso.titulo, descarga.fecha.strftime("%d/%m/%Y")])
    print(tabla_historial)