from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import buscar_recurso_por_id, buscar_recurso_por_titulo, obtener_listado_recursos
from modelos.recurso_digital import RecursoDigital
from ui.ingresar_datos import ingresar_datos_recurso, ingresar_id_recurso
from negocio.validaciones import validar_suscripcion, validar_eliminacion
from datos.eliminar_datos import eliminar_objeto
from negocio.tablas import tabla_recursos_digitales


def registrar_recursos():
    titulo, tipo = ingresar_datos_recurso()
    if buscar_recurso_por_titulo(titulo):
        return print("Recurso ya registrado.")
    else:
        nivel_suscripcion = validar_suscripcion()
    recurso_nuevo = RecursoDigital(titulo=titulo, tipo=tipo, nivel_suscripcion=nivel_suscripcion)
    insertar_objeto(recurso_nuevo)


def listar_recursos():
    if obtener_listado_recursos():
        print("\nRecursos digitales disponibles:\n", tabla_recursos_digitales())
    else:
        print("No hay recursos disponibles. ")


def actualizar_recursos():
    try:
        recurso = buscar_recurso_por_id(ingresar_id_recurso())
        if not recurso:
            return print("Recurso no encontrado.")
        suscripcion_nueva = validar_suscripcion()
        recurso.nivel_suscripcion = suscripcion_nueva
        actualizar_objeto()
    except ValueError:
        print("ID invalida")


def eliminar_recursos():
    recurso = buscar_recurso_por_id(ingresar_id_recurso())
    if not recurso:
        return print("Recurso no encontrado.")
    eliminar = validar_eliminacion()
    if eliminar:
        eliminar_objeto(recurso)