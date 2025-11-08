from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import obtener_listado_recursos, buscar_recurso_por_id
from modelos.recurso_digital import RecursoDigital
from prettytable import PrettyTable
from ui.ingresar_datos import ingresar_datos_recurso, ingresar_recurso
from negocio.validaciones import validar_suscripcion


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
    recursos = obtener_listado_recursos()
    tabla_recursos = PrettyTable(["ID", "Titulo", "Tipo", "Suscripcion"])
    for recurso in recursos:
        tabla_recursos.add_row([recurso.id, recurso.titulo, recurso.tipo, recurso.nivel_suscripcion])
    print(tabla_recursos)


def actualizar_recursos():
    try:
        id_recurso = ingresar_recurso()
        recurso = buscar_recurso_por_id(id_recurso)
        if not recurso:
            return print("Recurso no encontrado.")
        suscripcion_nueva = validar_suscripcion()
        recurso.nivel_suscripcion = suscripcion_nueva
        actualizar_objeto()
    except ValueError:
        print("ID invalida")


def eliminar_recurso():
    pass