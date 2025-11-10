import tkinter

ventana = tkinter.Tk()
ventana.title("Biblioteca Digital")
ventana.geometry("1024x768")
ventana.configure(bg="#e6e9ef")


# ==== FUNCIONES DE CAMBIO DE MENÚ ====
def mostrar_menu_principal():
    frame_usuarios.pack_forget()
    frame_recursos.pack_forget()
    frame_principal.pack(fill="both", expand=True)


def mostrar_menu_usuarios():
    frame_principal.pack_forget()
    frame_usuarios.pack(fill="both", expand=True)


def mostrar_menu_recursos():
    frame_principal.pack_forget()
    frame_recursos.pack(fill="both", expand=True)


# ==== ESTILOS ====
def efecto_boton(boton):
    boton.configure(
        bg="#d1d8e0",
        fg="#1e272e",
        font=("Segoe UI", 14, "bold"),
        relief="flat",
        activebackground="#a4b0be",
        activeforeground="white",
        bd=0,
        padx=10,
        pady=12,
        cursor="hand2"
    )


def hover_in(e):
    e.widget["bg"] = "#8395a7"
    e.widget["fg"] = "white"


def hover_out(e):
    e.widget["bg"] = "#d1d8e0"
    e.widget["fg"] = "#1e272e"


# ==== FRAME PRINCIPAL ====
frame_principal = tkinter.Frame(ventana, bg="#e6e9ef")

titulo = tkinter.Label(
    frame_principal,
    text="Biblioteca Digital",
    font=("Segoe UI", 26, "bold"),
    bg="#74b9ff",
    fg="white",
    pady=25,
)
titulo.pack(fill="x", pady=(0, 20))

botones_principales = [
    ("Gestionar usuarios", mostrar_menu_usuarios),
    ("Recursos digitales", mostrar_menu_recursos),
    ("Descargar recursos", None),
    ("Historial de descargas", None),
    ("Reseñas y valoraciones", None),
]

for texto, comando in botones_principales:
    b = tkinter.Button(frame_principal, text=texto, command=comando)
    efecto_boton(b)
    b.pack(fill="x", padx=250, pady=7)
    b.bind("<Enter>", hover_in)
    b.bind("<Leave>", hover_out)

boton_salir = tkinter.Button(
    frame_principal,
    text="Salir",
    bg="#ff7675",
    fg="white",
    font=("Segoe UI", 14, "bold"),
    relief="flat",
    padx=10,
    pady=10,
    command=ventana.destroy,
)
boton_salir.pack(pady=40, ipadx=10)
boton_salir.bind("<Enter>", lambda e: boton_salir.config(bg="#d63031"))
boton_salir.bind("<Leave>", lambda e: boton_salir.config(bg="#ff7675"))


frame_usuarios = tkinter.Frame(ventana, bg="#e6e9ef")
titulo_gestion_usuarios = tkinter.Label(frame_usuarios, text="Gestión de Usuarios", font=("Segoe UI", 26, "bold"), bg="#55efc4", fg="#2d3436", pady=25,)
titulo_gestion_usuarios.pack(fill="x", pady=(0, 20))


botones_usuarios = [ "Agregar usuario", "Listar usuarios", "Actualizar suscripciones", "Eliminar usuarios", "Volver atrás",]
for texto in botones_usuarios:
    comando = mostrar_menu_principal if texto == "Volver atrás" else None
    b = tkinter.Button(frame_usuarios, text=texto, command=comando)
    efecto_boton(b)
    b.pack(fill="x", padx=300, pady=7)
    b.bind("<Enter>", hover_in)
    b.bind("<Leave>", hover_out)


frame_recursos = tkinter.Frame(ventana, bg="#e6e9ef")
titulo_recursos = tkinter.Label(frame_recursos, text="Recursos Digitales", font=("Segoe UI", 26, "bold"), bg="#81ecec", fg="#2d3436", pady=25,)
titulo_recursos.pack(fill="x", pady=(0, 20))


botones_recursos = ["Registrar recurso", "Listar recursos", "Actualizar suscripciones", "Eliminar recursos", "Volver atrás",]
for texto in botones_recursos:
    comando = mostrar_menu_principal if texto == "Volver atrás" else None
    b = tkinter.Button(frame_recursos, text=texto, command=comando)
    efecto_boton(b)
    b.pack(fill="x", padx=300, pady=7)
    b.bind("<Enter>", hover_in)
    b.bind("<Leave>", hover_out)


frame_principal.pack(fill="both", expand=True)


ventana.mainloop()