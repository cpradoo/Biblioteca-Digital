from datos.conexion import sesion


def insertar_objeto(objeto):
    sesion.add(objeto)
    try:
        sesion.commit()
        print("Registrado correctamente.")
    except Exception as error:
        sesion.rollback()
        print(f"Error al guardar: {error}")
    finally:
        sesion.close()