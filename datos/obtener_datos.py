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


def buscar_usuario_por_id(id_usuario):
    return sesion.get(Usuario, id_usuario)


def buscar_recurso_por_id(id_recurso):
    return sesion.get(RecursoDigital, id_recurso)


def buscar_usuario_por_correo(correo):
    return sesion.query(Usuario).filter_by(correo=correo).first()


def buscar_recurso_por_titulo(titulo):
    return sesion.query(RecursoDigital).filter_by(titulo=titulo).first()