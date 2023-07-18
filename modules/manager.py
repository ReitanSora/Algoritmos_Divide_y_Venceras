# Tema: Técnicas de diseño de algoritmos - Divide y Vencerás
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Carrera: Ingeniería en Sistemas de la Información
# Paralelo: SI4 - 002
# Fecha de entrega: 19/07/2023

import tkinter as tk
from static import style
from modules.navegacion import Navegacion
from modules.home import Home
from modules.pi import Pi
from modules.karatsuba import Karatsuba
from modules.strassen import Strassen


class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        # metodo constructor de la clase Tk
        super().__init__(*args, **kwargs)
        self.title("Técnicas de Diseño de algoritmos - Divide y Vencerás")
        self.geometry("1000x600")
        #self.resizable(False, False)

        # contenedor para los botones de navegacion
        Navegacion(self)

        # contenedor donde se mostrarán todas las demás ventanas
        container = tk.Frame(self)
        container.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(background=style.BG, bd=0)
        container.config(width="800")

        # creacion de filas y clumnas disponibles en el frame container,
        # 0 = 1 columna/fila ; weight = espacio que ocupa
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # diccionario de clases
        self.frames = {}

        for F in (Home, Pi, Karatsuba, Strassen):
            frame = F(container, self)
            self.frames[F] = frame

            # configuracion de filas, columnas y rellenado del frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

    # metodo para mostrar las diferentes ventanas
    def show_frame(self, container):
        frame = self.frames[container]

        # para poner una pantalla encima de la otra
        frame.tkraise()

    def salir(self):
        self.destroy()

    def move_to_home(self):
        self.show_frame(Home)

    def move_to_pi(self):
        self.show_frame(Pi)

    def move_to_karatsuba(self):
        self.show_frame(Karatsuba)

    def move_to_strassen(self):
        self.show_frame(Strassen)
