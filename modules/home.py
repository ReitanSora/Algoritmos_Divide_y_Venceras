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


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    #función para inicializar los widges que se mostrarán en la ventana
    def init_widgets(self):

        # label titulo bienvenida
        tk.Label(
            self,
            text="Diseño de algoritmos, Divide y vencerás",
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, pady=(20, 30))

        # label titulo bienvenida
        tk.Label(
            self,
            text="En este programa se encuentran 3 ejercicios que hacen uso de esta técnica de diseño, entre esos podemos encontrar el cálculo de los decimales de pi, multiplicación de enteros largos haciendo uso del algoritmo de Karatsuba y la multiplicación de matrices de gran dimensión usando el algoritmo de Strassen",
            **style.STYLE_TEXT,
        ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        info_frame = tk.Frame(self, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=20)

        tk.Label(info_frame,
                 text="Temas incluidos:\n\n     • Cálculo de decimales Pi\n     • Multiplicación de enteros largos\n     • Multiplicación de matrices",
                 **style.STYLE_TEXT,
                 ).grid(row=0, column=0, sticky=tk.NW, pady=(0,20))

        tk.Label(info_frame,
                 text="Librerías usadas:\n\n     • tkinter\n     • mpmath\n     • numpy\n",
                 **style.STYLE_TEXT,
                 ).grid(row=1, column=0, sticky=tk.NW)
        
        tk.Label(info_frame,
                 text="Integrantes:\n\n     • Stiven Anthony Pilca Sánchez\n     • Juan Ariel Tulcanaza Paucar\n",
                 **style.STYLE_TEXT,
                 ).grid(row=2, column=0, sticky=tk.NW)