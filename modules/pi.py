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
from functions import events as event
from functions import funcion_pi


class Pi(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def calcular(self):
        self.container_frame.bind('<Configure>', lambda e: self.container.configure(
            scrollregion=self.container.bbox(tk.ALL)))

        self.texto_resultado.set(funcion_pi.calcular_pi(self.decimales.get()))
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.container.configure(yscrollcommand=self.scroll.set)
        self.container.bind('<Configure>', lambda e: self.container.configure(
            scrollregion=self.container.bbox(tk.ALL)))
        
    def init_widgets(self):

        tk.Label(self,
                 text="Cálculo del número Pi",
                 **style.STYLE_TITTLE
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)

        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        DECIMALES = {
            "5 000": 5000,
            "10 000": 10000,
            "15 000": 15000,
        }

        borde_seleccion = tk.LabelFrame(
            input_frame, text="Número de decimales", **style.STYLE_ENTRY_BORDER)
        borde_seleccion.grid(row=0, column=0)

        self.decimales = tk.IntVar(value=15000)
        for (keys, values) in DECIMALES.items():
            tk.Radiobutton(borde_seleccion,
                           text=keys,
                           variable=self.decimales,
                           value=values,
                           **style.STYLE_RADIO_BUTTON,
                           ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=(30,0))

        # boton para calcular
        borde_1 = tk.LabelFrame(input_frame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, column=1, pady=(30,0), padx=20)

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.calcular,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        self.container = tk.Canvas(
            self, background=style.BG, bd=0, relief="flat", highlightthickness=0)
        self.container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.container_frame = tk.Frame(self.container, background=style.BG)
        self.container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20)

        self.container.create_window((0, 0), window=self.container_frame)

        self.texto_resultado = tk.StringVar()
        tk.Label(self.container_frame,
                 textvariable=self.texto_resultado,
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10)

        self.scroll = tk.Scrollbar(self,
                                   border=0,
                                   orient="vertical",
                                   command=self.container.yview,
                                   )
        
