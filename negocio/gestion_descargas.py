from modelos.usuario import Usuario
from modelos.recurso_digital import RecursoDigital
from modelos.historial import HistorialDescargas
from prettytable import PrettyTable


def descargar_recurso_digital(session, id_usuario, id_recurso):
    usuario = session.query(Usuario).filter_by(id=id_usuario).first()
    recurso = session.query(RecursoDigital).filter_by(id=id_recurso).first()
    if not usuario or not recurso:
        print("Usuario o recurso no encontrado.")
        return
    if recurso.nivel_suscripcion == "premium" and usuario.nivel_suscripcion != "premium":
        print(f"{recurso.titulo} solo esta disponible para usuarios premium.")
        return
    nueva_descarga = HistorialDescargas(id_usuario=usuario.id, id_recurso=recurso.id)
    session.add(nueva_descarga)
    session.commit()
    print(f"{recurso.titulo} descargado correctamente.")


def listar_historial_descargas(session):
    historial = (
        session.query(HistorialDescargas, Usuario, RecursoDigital)
        .join(Usuario, HistorialDescargas.id_usuario == Usuario.id)
        .join(RecursoDigital, HistorialDescargas.id_recurso == RecursoDigital.id)
        .all())
    if not historial:
        print("No hay descargas registradas aún.")
        return
    tabla = PrettyTable()
    tabla.field_names = ["Usuario", "Recurso Digital", "Fecha"]
    for descarga, usuario, recurso in historial:
        fecha= descarga.fecha_descarga.strftime("%d/%m/%Y")
        tabla.add_row([usuario.nombre, recurso.titulo, fecha])
    print(tabla)