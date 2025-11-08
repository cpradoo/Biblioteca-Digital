def validar_suscripcion():
    while True:
        nivel_suscripcion = input("Suscripcion (gratuita/premium): ").lower()
        if not nivel_suscripcion:
            return "gratuita"
        elif nivel_suscripcion in ["gratuita", "premium"]:
            return nivel_suscripcion
        else:
            print("Valor invalido, intente nuevamente.")