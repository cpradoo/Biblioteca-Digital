from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import buscar_usuario_por_id, buscar_recurso_por_id
from modelos.historial import HistorialDescargas
from datetime import datetime
from ui.ingresar_datos import ingresar_id_usuario, ingresar_id_recurso
from negocio.listados import tabla_recursos_digitales, tabla_historial_descargas


def descargar_recurso():
    try:
        usuario = buscar_usuario_por_id(ingresar_id_usuario)
        if not usuario:
            return print("Usuario no encontrado.")
        tabla = tabla_recursos_digitales()
        print(tabla)
        recurso = buscar_recurso_por_id(ingresar_id_recurso())
        if not recurso:
            return print("Recurso no encontrado.")
        if recurso.nivel_suscripcion == "premium" and usuario.nivel_suscripcion != "premium":
            return print("Necesita suscripcion premium.")
        descarga_nueva = HistorialDescargas(id_usuario=usuario.id,id_recurso=recurso.id,fecha=datetime.now())
        insertar_objeto(descarga_nueva)
    except ValueError:
        print("ID invalida")


def listar_historial():
    tabla = tabla_historial_descargas()
    print(tabla)