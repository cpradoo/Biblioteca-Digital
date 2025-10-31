from datos.conexion import sesion


def actualizar_objeto():
    try:
        sesion.commit()
        print("Actualizado correctamente.")
    except Exception as error:
        sesion.rollback()
        print(f"Error al actualizar: {error}")
    finally:
        sesion.close()