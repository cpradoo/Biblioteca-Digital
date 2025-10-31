from datos.conexion import sesion
from modelos.usuario import Usuario
from modelos.recurso_digital import RecursoDigital
from modelos.historial import HistorialDescargas


def obtener_listado_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos


def obtener_listado_usuarios():
    listado_usuarios = sesion.query(Usuario).all()
    if len(listado_usuarios) > 0:
        return listado_usuarios


def obtener_listado_recursos():
    listado_recursos = sesion.query(RecursoDigital).all()
    if len(listado_recursos) > 0:
        return listado_recursos


def obtener_historial():
    listado_historial = sesion.query(HistorialDescargas).all()
    if len(listado_historial) > 0:
        return listado_historial