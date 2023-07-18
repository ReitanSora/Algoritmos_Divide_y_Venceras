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
from functions import funcion_multiplicacion_matrices as algoritmo


class Strassen(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def mostrar_matriz(self, matriz_original):
        matriz_modificada = []
        for i in range(len(matriz_original)):
            matriz_modificada.append([])
            for j in range (len(matriz_original)):
                matriz_modificada[i].append(matriz_original[i][j])

        return matriz_modificada

    def calcular(self):
        self.container_frame.bind('<Configure>', lambda e: self.container.configure(
            scrollregion=self.container.bbox(tk.ALL)))
        try:
            dimension = int(self.dimension.get())

            matriz_a = algoritmo.generar_matrices(dimension)
            matriz_b = algoritmo.generar_matrices(dimension)
            resultado = algoritmo.strassen(matriz_a, matriz_b)

            matriz_a_mostrar = self.mostrar_matriz(matriz_a)
            matriz_b_mostrar = self.mostrar_matriz(matriz_b)
            matriz_resultado_mostrar = self.mostrar_matriz(resultado)
            self.texto_resultado.set("Matriz A\n\n{}\n\nMatriz B\n\n{}\n\nResultado\n\n{}".format(matriz_a_mostrar, matriz_b_mostrar,matriz_resultado_mostrar))

        except ValueError:
            self.texto_alerta_dimension.set("Ingrese un número entero")

        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        #self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.container.configure(yscrollcommand=self.scroll.set)
        #self.container.configure(xscrollcommand=self.scroll_x.set)
        self.container.bind('<Configure>', lambda e: self.container.configure(
            scrollregion=self.container.bbox(tk.ALL)))

    # función para verificar el dato ingresado por el usuario
    def verificacion(self):
        try:
            if self.dimension.get() == "":
                self.texto_alerta_dimension.set("Ingrese un valor")
            else:
                if int(self.dimension.get()) > 120:
                    self.texto_alerta_dimension.set(
                        "Ingrese un valor menor o igual a 120")
                else:
                    self.texto_alerta_dimension.set("")
                    self.calcular()
        except ValueError:
            self.texto_alerta_dimension.set(
                "Ingrese un valor numérico correcto")

    def init_widgets(self):
        tk.Label(self,
                 text="Multiplicación de matrices",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)

        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        tk.Label(input_frame,
                 text="Tamaño de la matríz",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0)

        # entry dimension
        borde_entry_1 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_1.grid(row=0, column=1, pady=(20, 0))

        self.dimension = tk.StringVar()
        dato = tk.Entry(borde_entry_1,
                 textvariable=self.dimension,
                 **style.STYLE_ENTRY,
                 )
        dato.pack(side=tk.TOP, expand=True)
        dato.focus_set()

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=200)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 200, 0, **style.STYLE_CANVAS_LINE)

        # label alerta multiplicando
        self.texto_alerta_dimension = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_dimension,
                 **style.STYLE_WARNING
                 ).pack()

        # boton para calcular
        borde_1 = tk.LabelFrame(input_frame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, column=2, pady=(0), padx=20)

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.verificacion,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        self.container = tk.Canvas(
            self, background=style.BG, bd=0, relief="flat", highlightthickness=0)
        self.container.pack(side=tk.LEFT, fill=tk.BOTH,
                            expand=True, padx=20, pady=20)

        self.container_frame = tk.Frame(self.container, background=style.BG)
        self.container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20)

        self.container.create_window((0, 0), window=self.container_frame)

        self.texto_resultado = tk.StringVar()
        resultado = tk.Label(self.container_frame,
                 textvariable=self.texto_resultado,
                 **style.STYLE_TEXT,
                 )
        resultado.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10)

        resultado.configure(wraplength="550p")
        

        self.scroll = tk.Scrollbar(self,
                                   border=0,
                                   orient="vertical",
                                   command=self.container.yview,
                                   )

        # self.scroll_x = tk.Scrollbar(self,
        #                              border=0,
        #                              orient="horizontal",
        #                              command=self.container.xview,
        #                              )

        
