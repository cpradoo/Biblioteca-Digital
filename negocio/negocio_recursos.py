from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import obtener_listado_recursos, buscar_recurso_por_id
from modelos.recurso_digital import RecursoDigital
from ui.ingresar_datos import ingresar_datos_recurso, ingresar_id_recurso
from negocio.validaciones import validar_suscripcion, validar_eliminacion
from datos.eliminar_datos import eliminar_objeto
from negocio.listados import tabla_recursos_digitales


def registrar_recurso():
    titulo, tipo = ingresar_datos_recurso()
    nivel_suscripcion = validar_suscripcion()
    recursos = obtener_listado_recursos()
    if recursos:
        for recurso in recursos:
            if recurso.titulo.lower() == titulo.lower():
                return print("Recurso ya registrado.")
    recurso_nuevo = RecursoDigital(titulo=titulo, tipo=tipo, nivel_suscripcion=nivel_suscripcion)
    insertar_objeto(recurso_nuevo)


def listar_recursos():
    tabla = tabla_recursos_digitales()
    print(tabla)


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


def eliminar_recurso():
    recurso = buscar_recurso_por_id(ingresar_id_recurso())
    if not recurso:
        return print("Recurso no encontrado.")
    eliminar = validar_eliminacion()
    if eliminar:
        eliminar_objeto(recurso)