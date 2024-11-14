from tkinter import *
from Funciones import *

root = Tk()
root.geometry("300x120")
root.title("Descarga de camiones")

validacion = root.register(solo_numeros)

miFrame = Frame(root)
miFrame.pack()

# Entradas de texto
cuadroCantidad = Entry(miFrame, validate="key", validatecommand=(validacion, "%S"))
cuadroCantidad.grid(row=0, column=1, pady=2, padx=2)

cuadroCamionVacio = Entry(miFrame, validate="key", validatecommand=(validacion, "%S"))
cuadroCamionVacio.grid(row=1, column=1, pady=2, padx=2)

cuadroCamionLleno = Entry(miFrame, validate="key", validatecommand=(validacion, "%S"))
cuadroCamionLleno.grid(row=2, column=1, pady=2, padx=2)

# Etiquetas de texto
cantidadLabel = Label(miFrame, text="Cantidad de camiones: ")
cantidadLabel.grid(row=0, column=0, sticky="w", pady=2, padx=2)

camionVacioLabel = Label(miFrame, text="Peso del camión vacío (Kg): ")
camionVacioLabel.grid(row=1, column=0, sticky="w", pady=2, padx=2)

camionLlenoLabel = Label(miFrame, text="Peso del camión lleno (Kg): ")
camionLlenoLabel.grid(row=2, column=0, sticky="w", pady=2, padx=2)

# Botón de inicio
botonesFrame = Frame(miFrame)
botonesFrame.grid(row=6, column=0, columnspan=2, pady=10)


def iniciar_proceso():
    # Función que inicia el proceso de descarga de los camiones
    try:
        cantidad = int(cuadroCantidad.get())
        camion_vacio = int(cuadroCamionVacio.get())
        camion_lleno = int(cuadroCamionLleno.get())

        if camion_lleno <= camion_vacio:
            messagebox.showerror(
                "Error",
                "El peso del camión lleno debe ser mayor al peso del camión vacío.",
            )
            return
        else:
            control_descarga = ControlDescarga(
                cantidad,
                camion_vacio,
                camion_lleno,
                cuadroCantidad,
                botonIniciarDescarga,
            )
            control_descarga.iniciar_descarga()
    except ValueError:
        messagebox.showerror(
            "Error", "Ingrese solo valores numéricos en todos los campos."
        )


botonIniciarDescarga = Button(
    botonesFrame, text="Iniciar Descarga", width=20, command=iniciar_proceso
)
botonIniciarDescarga.grid(padx=5)

root.mainloop()
