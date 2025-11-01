from datos.conexion import sesion
from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_listado_recursos
from modelos.historial import HistorialDescargas
from modelos.recurso_digital import RecursoDigital
from modelos.usuario import Usuario
from prettytable import PrettyTable
from datetime import datetime


def descargar_recursos():
    id_usuario = input("Ingrese su ID: ")
    usuario = sesion.get(Usuario, id_usuario)
    if not usuario:
        return print("ID Invalida.")
    recursos = obtener_listado_recursos()
    tabla_recursos = PrettyTable(["ID", "Titulo", "Tipo", "Suscripcion"])
    for recurso in recursos:
        tabla_recursos.add_row([recurso.id, recurso.titulo, recurso.tipo, recurso.nivel_suscripcion])
    id_recurso = input("Ingrese la ID del recurso: ")
    recurso = sesion.get(RecursoDigital, id_recurso)
    if not recurso:
        return print("ID Invalida.")
    if recurso.nivel_suscripcion == "premium" and usuario.nivel_suscripcion != "premium":
        return print("No disponible con tu suscripcion actual.")
    descarga_nueva = HistorialDescargas(id_usuario=usuario.id,id_recurso=recurso.id,fecha=datetime.now())
    insertar_objeto(descarga_nueva)
    print("Descargado correctamente.")


def listar_historial():
    descargas = sesion.query(HistorialDescargas).all()
    if not descargas:
        print("No hay descargas registradas.")
        return
    tabla = PrettyTable(["Usuario", "Recurso Digital", "Fecha"])
    for descarga in descargas:
        tabla.add_row([descarga.usuario.nombre, descarga.recurso.titulo, descarga.fecha.strftime("%d/%m/%Y")])
    print(tabla)