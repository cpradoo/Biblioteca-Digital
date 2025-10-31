from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version


def menu_principal():
    print(f"\n{nombre_aplicacion} v.{numero_version}")
    print("================================")
    print("[1] Gestionar Usuarios")
    print("[2] Gestionar Recursos Digitales")
    print("[3] Descargas")
    print("[4] Salir")


def menu_gestion_usuarios():
    print("\nGestion de usuarios")
    print("================================")
    print("[1] Registrar usuario")
    print("[2] Listar usuarios")
    print("[3] Actualizar suscripcion")
    print("[4] Volver atras")


def menu_descargas():
    print("\nDescargas")
    print("================================")
    print("[1] Descargar recurso digital")
    print("[2] Historial de descargas")
    print("[3] Volver atras")