from tkinter import END, messagebox
import random
import threading
import time


class CalculoCafe:

    def __init__(self, cantidad_camiones, camion_vacio, camion_lleno, tipo_peso):
        # Función que inicializa los valores de la clase
        self.cantidad = cantidad_camiones
        self.camion_vacio = camion_vacio
        self.camion_lleno = camion_lleno
        self.tipo_peso = tipo_peso
        self.contenedores_defectuosos_usados = 1
        self.contenedores_especiales_usados = 1
        self.sacos_defectuosos = 0
        self.sacos_especiales = 0
        self.sacos_en_contenedor_defectuoso = 0
        self.sacos_en_contenedor_especial = 0
        self.camiones_procesados = 0

    def calcular_carga_cafe(self):
        # Calcula la carga de café en el camión
        if self.tipo_peso == 1:
            carga_cafe = self.camion_lleno - self.camion_vacio
            print(f"Carga de café en kilo calculada: {carga_cafe}")
        else:
            carga_cafe = (self.camion_lleno - self.camion_vacio) * 1000
            print(f"Carga de café en ton calculada: {carga_cafe}")
        return carga_cafe

    def calcular_cantidad_sacos(self, carga_cafe):
        # Calcula la cantidad de sacos de café en el camión
        return carga_cafe // 70

    def clasificar_sacos(self, sacos_totales):
        # Clasifica los sacos de café en defectuosos y especiales
        for _ in range(sacos_totales):
            peso_saco = random.randint(65, 75)
            if peso_saco == 70:
                self.sacos_especiales += 1
                self.sacos_en_contenedor_especial += 1
            else:
                self.sacos_defectuosos += 1
                self.sacos_en_contenedor_defectuoso += 1

            if self.sacos_en_contenedor_especial >= 1000:
                self.contenedores_especiales_usados += 1
                messagebox.showinfo(
                    "Alerta",
                    "Contenedor de sacos especiales lleno. Cambia el contenedor",
                )
                self.sacos_en_contenedor_especial = 0

            if self.sacos_en_contenedor_defectuoso >= 1000:
                self.contenedores_defectuosos_usados += 1
                messagebox.showinfo(
                    "Alerta",
                    "Contenedor de sacos defectuosos lleno. Cambia el contenedor",
                )
                self.sacos_en_contenedor_defectuoso = 0

    def procesar_camion(self):
        # Procesa el camión y calcula la cantidad de sacos de café
        carga_cafe = self.calcular_carga_cafe()
        sacos_totales = self.calcular_cantidad_sacos(carga_cafe)
        self.clasificar_sacos(sacos_totales)

        self.camiones_procesados += 1
        messagebox.showwarning(
            "Alerta",
            f"El camión {self.camiones_procesados} ha sido descargado completamente. Continúa el siguiente.",
        )

    def registrar_totales(self):
        # Registra los totales de sacos de café procesados
        messagebox.showinfo(
            "Resumen",
            f"Camiones descargados: {self.camiones_procesados}\n"
            f"Sacos defectuosos: {self.sacos_defectuosos}\n"
            f"Sacos especiales: {self.sacos_especiales}\n"
            f"Contenedores para sacos defectuosos utilizados: {self.contenedores_defectuosos_usados}\n"
            f"Contenedores para sacos especiales utilizados: {self.contenedores_especiales_usados}",
        )


class ControlDescarga:
    # Clase que controla la descarga de los camiones
    def __init__(
        self,
        cantidad_camiones,
        camion_vacio,
        camion_lleno,
        cuadroCantidad,
        cuadroCamionVacio,
        cuadroCamionLleno,
        tipo_peso,
        boton,
        radiobutton_kg,
        radiobutton_ton,
    ):
        # Función que inicializa los valores de la clase
        self.cuadroCantidad = cuadroCantidad
        self.cuadroCamionVacio = cuadroCamionVacio
        self.cuadroCamionLleno = cuadroCamionLleno
        self.boton = boton
        self.radiobutton_kg = radiobutton_kg
        self.radiobutton_ton = radiobutton_ton
        self.calculo = CalculoCafe(
            cantidad_camiones, camion_vacio, camion_lleno, tipo_peso
        )

    def iniciar_descarga(self):
        # Función que inicia la descarga de los camiones

        # Deshabilitar el campo de cantidad de camiones en la interfaz
        self.cuadroCantidad.config(state="disabled")
        self.radiobutton_kg.config(state="disabled")
        self.radiobutton_ton.config(state="disabled")

        # Cambiar el botón a "Continuar Descarga"
        self.boton.config(text="Continuar Descarga", command=self.continuar_descarga)

        # Iniciar la primera descarga
        self.continuar_descarga()

    def continuar_descarga(self):
        # Función que continúa la descarga de los camiones
        if self.calculo.camiones_procesados >= self.calculo.cantidad:
            self.boton.config(text="Ver Resumen", command=self.ver_resumen)
            self.calculo.registrar_totales()
            return

        # Solicitar nuevos valores de camion_vacio y camion_lleno
        try:
            camion_vacio = int(self.cuadroCamionVacio.get())
            camion_lleno = int(self.cuadroCamionLleno.get())
            if camion_lleno <= camion_vacio:
                messagebox.showerror(
                    "Error",
                    "El peso del camión lleno debe ser mayor al peso del camión vacío.",
                )
                return
            else:
                self.calculo.camion_vacio = camion_vacio
                self.calculo.camion_lleno = camion_lleno
        except ValueError:
            messagebox.showerror(
                "Error", "Ingrese solo valores numéricos en todos los campos."
            )
            return

        # Temporizador de 1 segundos en un hilo separado para evitar congelamiento de la interfaz
        def temporizador():
            time.sleep(1)
            self.calculo.procesar_camion()

        hilo_temporizador = threading.Thread(target=temporizador)
        hilo_temporizador.start()

    def ver_resumen(self):
        # Función que muestra el resumen de la descarga de los camiones
        self.calculo.registrar_totales()


def solo_numeros(char):
    # Función que valida si un caracter es un número
    return char.isdigit()
