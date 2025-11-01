from datos.conexion import sesion
from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import obtener_listado_recursos
from modelos.recurso_digital import RecursoDigital
from prettytable import PrettyTable


def registrar_recurso():
    print()
    titulo = input("Titulo: ")
    tipo = input("Tipo: ")
    nivel_suscripcion = input("Suscripcion (gratuita/premium): ")
    if not titulo or not tipo:
        print("Ingrese titulo y tipo de recurso a registrar.")
        return
    if not nivel_suscripcion:
        nivel_suscripcion = "gratuita"
    else:
        nivel_suscripcion = nivel_suscripcion.lower()
        if nivel_suscripcion not in ["gratuita", "premium"]:
            print("Tipo de suscripcion invalida.")
            return
    recursos = obtener_listado_recursos()
    if recursos:
        for recurso in recursos:
            if recurso.titulo.lower() == titulo.lower():
                print("Recurso ya registrado.")
                return
    recurso_nuevo = RecursoDigital(titulo=titulo, tipo=tipo, nivel_suscripcion=nivel_suscripcion)
    insertar_objeto(recurso_nuevo)


def listar_recursos():
    recursos = obtener_listado_recursos()
    tabla_recursos = PrettyTable(["ID", "Titulo", "Tipo", "Suscripcion"])
    for recurso in recursos:
        tabla_recursos.add_row([recurso.id, recurso.titulo, recurso.tipo, recurso.nivel_suscripcion])
    print("\nRecursos Digitales: ")
    print(tabla_recursos)


def actualizar_recursos():
    try:
        id_recurso = int(input("ID del usuario: "))
        suscripcion_nueva = input("Nueva suscripcion: ").lower()
        recurso = sesion.get(RecursoDigital, id_recurso)
        if not recurso:
            print("Recurso no encontrado")
            return
        if suscripcion_nueva not in ["gratuita", "premium"]:
            print("Tipo de suscripcion invalida.")
            return
        recurso.nivel_suscripcion = suscripcion_nueva
        actualizar_objeto()
    except ValueError:
        print("ID invalida")