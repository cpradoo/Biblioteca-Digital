from negocio.gestion_usuarios import registrar_usuarios, listar_usuarios, actualizar_usuarios
from negocio.gestion_recursos import registrar_recurso, listar_recursos, actualizar_recursos


def menu_gestion_usuarios():
    print("\nGestionar Usuarios")
    print("================================")
    print("[1] Registrar usuario")
    print("[2] Listar usuarios")
    print("[3] Actualizar suscripcion")
    print("[4] Volver atras")


def menu_gestion_recursos():
    print("\nRecursos Digitales")
    print("================================")
    print("[1] Registrar recurso digital")
    print("[2] Listar recursos digitales")
    print("[3] Actualizar suscripcion")
    print("[4] Volver atras")


def gestionar_usuarios():
    while True:
        menu_gestion_usuarios()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar_usuarios()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            actualizar_usuarios()
        elif opcion == "4":
            break
        else:
            print("Opcion invalida.")


def gestionar_recursos():
    while True:
        menu_gestion_recursos()
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            registrar_recurso()
        elif opcion == "2":
            listar_recursos()
        elif opcion == "3":
            actualizar_recursos()
        elif opcion == "4":
            break
        else:
            print("Opcion invalida.")