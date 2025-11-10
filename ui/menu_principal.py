from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version
from ui.submenus import gestionar_usuarios, gestionar_recursos
from negocio.negocio_descargas import descargar_recursos, listar_historial


def menu_principal():
    print(f"\n{nombre_aplicacion} v.{numero_version}")
    print("================================")
    print("[1] Gestionar Usuarios")
    print("[2] Recursos Digitales")
    print("[3] Descargas")
    print("[4] Historial")
    print("[5] Reseñas")
    print("[0] Salir")


def iniciar_menu():
    while True:
        menu_principal()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            gestionar_usuarios()
        elif opcion == "2":
            gestionar_recursos()
        elif opcion == "3":
            descargar_recursos()
        elif opcion == "4":
            listar_historial()
        elif opcion == "5":
            pass
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("\nOpcion invalida, intente nuevamente.")