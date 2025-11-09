def validar_suscripcion():
    while True:
        nivel_suscripcion = input("Suscripcion (gratuita/premium): ").lower()
        if not nivel_suscripcion:
            return "gratuita"
        elif nivel_suscripcion in ("gratuita", "premium"):
            return nivel_suscripcion
        else:
            print("Valor invalido, intente nuevamente.")


def validar_eliminacion():
    while True:
        confirmacion = input("\nSe requiere confirmacion adicional: \n1 = Confirmar | 0 = Volver Atras: ")
        if confirmacion == "1":
            return True
        elif confirmacion == "0":
            print("Cancelado.")
            return False
        else:
            print("\nOpcion invalida, intente nuevamente.")