from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version


def menu_principal():
    print(f"{nombre_aplicacion} v.{numero_version}")
    print("=======================================")
    print("[1] Gestionar Usuarios")
    print("[2] Gestionar Recursos Digitales")
    print("[3] Descargas")
    print("[4] Historial de Descargas")
    print("[0] Salir")