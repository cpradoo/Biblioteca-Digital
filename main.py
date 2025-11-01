from ui.menu_principal import menu_principal
from ui.menus_extras import gestionar_usuarios, gestionar_recursos
from negocio.gestion_descargas import descargar_recursos, listar_historial


def main():
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
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion Invalida.")


main()