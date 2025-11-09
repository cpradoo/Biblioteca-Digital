from datos.conexion import sesion

def eliminar_objeto(objeto):
    sesion.delete(objeto)
    try:
        sesion.commit()
        print("Eliminado correctamente")
    except Exception as e:
        sesion.rollback()
        print(f"Error al eliminar: {e}")
    finally:
        sesion.close()