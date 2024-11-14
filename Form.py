from tkinter import *
from Funciones import *

root = Tk()
root.geometry("300x150")
root.title("Descarga de camiones")

validacion = root.register(solo_numeros)

# Variable para los Radiobuttons
tipo_peso = IntVar()

miFrame = Frame(root)
miFrame.pack()


# Entradas de texto
cuadroCantidad = Entry(miFrame, validate="key", validatecommand=(validacion, "%S"))
cuadroCantidad.grid(row=0, column=1, pady=2, padx=2)

cuadroCamionVacio = Entry(miFrame, validate="key", validatecommand=(validacion, "%S"))
cuadroCamionVacio.grid(row=2, column=1, pady=2, padx=2)

cuadroCamionLleno = Entry(miFrame, validate="key", validatecommand=(validacion, "%S"))
cuadroCamionLleno.grid(row=3, column=1, pady=2, padx=2)

# Etiquetas de texto
cantidadLabel = Label(miFrame, text="Cantidad de camiones: ")
cantidadLabel.grid(row=0, column=0, sticky="w", pady=2, padx=2)

camionVacioLabel = Label(miFrame, text="Peso del camión vacío: ")
camionVacioLabel.grid(row=2, column=0, sticky="w", pady=2, padx=2)

camionLlenoLabel = Label(miFrame, text="Peso del camión lleno: ")
camionLlenoLabel.grid(row=3, column=0, sticky="w", pady=2, padx=2)

# Etiqueta y Radiobuttons en la misma fila
tipoCamionLabel = Label(miFrame, text="Medida de peso: ")
tipoCamionLabel.grid(row=1, column=0, sticky="w", pady=2, padx=2)

# Frame para los Radiobuttons
selectorFrame = Frame(miFrame)
selectorFrame.grid(row=1, column=1, columnspan=2, pady=2, padx=2)
Radiobutton_kg = Radiobutton(selectorFrame, text="Kg", variable=tipo_peso, value=1)
Radiobutton_kg.grid(row=1, column=1, padx=5)
Radiobutton_Ton = Radiobutton(selectorFrame, text="Ton", variable=tipo_peso, value=2)
Radiobutton_Ton.grid(row=1, column=2, padx=5)

# Botón de inicio
botonesFrame = Frame(miFrame)
botonesFrame.grid(row=4, column=0, columnspan=2, pady=10)


def iniciar_proceso():
    # Función que inicia el proceso de descarga de los camiones
    try:
        if not cuadroCantidad.get() or not cuadroCamionVacio.get() or not cuadroCamionLleno.get() or not tipo_peso.get():
            messagebox.showerror("Error", "Ingrese todos los campos.")
            return
        
        cantidad = int(cuadroCantidad.get())
        camion_vacio = int(cuadroCamionVacio.get())
        camion_lleno = int(cuadroCamionLleno.get())
        peso_seleccionado = tipo_peso.get()

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
                cuadroCamionVacio,
                cuadroCamionLleno,
                peso_seleccionado,
                botonIniciarDescarga,
                Radiobutton_kg,
                Radiobutton_Ton
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
