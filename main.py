from ui.menus import menu_principal, menu_gestion_usuarios, menu_descargas
from negocio.gestion_usuarios import registrar_usuarios, listar_usuarios, actualizar_usuarios
from negocio.gestion_descargas import listar_historial_descargas


while True:
    menu_principal()
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        menu_gestion_usuarios()
        op = input("Seleccione una opcion: ")
        if op == "1":
            print()
            registrar_usuarios()
        elif op == "2":
            listar_usuarios()
        elif op == "3":
            actualizar_usuarios()
        elif op == "4":
            continue
        else:
            print("Opcion invalida.")
    elif opcion == "2":
        pass
    elif opcion == "3":
        menu_descargas()
        op = input("Seleccione una opcion: ")
        if op == "1":
            pass
        elif op == "2":
            #listar_historial_descargas()
            pass
        elif op == "3":
            continue
        else:
            print("Opcion invalida.")
    elif opcion == "4":
        break