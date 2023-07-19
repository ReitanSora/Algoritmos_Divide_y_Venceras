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
from functions import funcion_enteros_largos as algoritmo


class Karatsuba(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    # función para calcular la multiplicación
    def calcular(self):
        # longitud de los numeros ingresados
        longitud = max(len(self.multiplicando.get()),
                       len(self.multiplicador.get()))
        longitud_modificada = longitud//2

        # variables que almacenan los valores ingresados por el usuario
        valor_multiplicando = int(self.multiplicando.get())
        valor_multiplicador = int(self.multiplicador.get())

        # escribir los datos en cada uno de los campos
        a = valor_multiplicando//10**longitud_modificada
        b = valor_multiplicando % 10**longitud_modificada
        c = valor_multiplicador//10**longitud_modificada
        d = valor_multiplicador % 10**longitud_modificada

        self.valor_a_b.set("a= {}, b= {}".format(a, b))
        self.valor_c_d.set("c= {}, d= {}".format(c, d))
        self.valor_formula.set("ac x 10^{} + [(a + b)(c + d) -ac -bd] x 10^{} + bd".format(
            2*longitud_modificada, longitud_modificada))

        # escribir los valores para acada parte de la fórmula
        self.valor_parte_1.set(
            "ac x 10^{}  =  {}".format(longitud_modificada*2, a*c*pow(10, longitud_modificada*2)))

        self.valor_parte_2.set(
            "[(a + b)(c + d) -ac -bd] x 10^{}  =  {}".format(longitud_modificada, ((a+b) * (c+d) - a*c - b*d)*pow(10, longitud_modificada)))

        self.valor_parte_3.set("bd  =  {}".format(b+d))

        # escribir el resultado en su campo
        self.valor_resultado.set(algoritmo.karatsuba_multiplicacion(
            valor_multiplicando, valor_multiplicador))

    # verificacion de los datos ingresados por el usuario
    def verificacion(self):
        try:
            if self.multiplicando.get() == "" and self.multiplicador.get() == "":
                self.texto_alerta_multiplicando.set("Ingrese un número entero")
                self.texto_alerta_multiplicador.set("Ingrese un número entero")
            else:
                # vaciar los textos de alerta
                self.texto_alerta_multiplicando.set("")
                self.texto_alerta_multiplicador.set("")
                self.calcular()
        except ValueError:
            self.texto_alerta_multiplicando.set("Ingrese un número entero")
            self.texto_alerta_multiplicador.set("Ingrese un número entero")

    # inicialización de los widgets de la ventana
    def init_widgets(self):
        tk.Label(self,
                 text="Multiplicación de enteros largos",
                 **style.STYLE_TITTLE
                 ).pack(side=tk.TOP, fill=tk.X, pady=30)

        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.columnconfigure(3, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        tk.Label(input_frame,
                 text="Multiplicando",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=0, column=0)

        tk.Label(input_frame,
                 text="Multiplicador",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=1, column=0)

        tk.Label(input_frame,
                 text="Fórmula",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=2, column=0, pady=(25, 0))

        tk.Label(input_frame,
                 text="Parte 1",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=3, column=0, pady=(25, 0))

        tk.Label(input_frame,
                 text="Parte 2",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=4, column=0, pady=(25, 0))

        tk.Label(input_frame,
                 text="Parte 3",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=5, column=0, pady=(25, 0))

        tk.Label(input_frame,
                 text="Resultado",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=6, column=0, pady=(25, 0))

        # entry multiplicando
        borde_entry_1 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_1.grid(row=0, column=1, pady=(20, 0))

        self.multiplicando = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.multiplicando,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=200)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 200, 0, **style.STYLE_CANVAS_LINE)

        # label alerta multiplicando
        self.texto_alerta_multiplicando = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_multiplicando,
                 **style.STYLE_WARNING
                 ).pack()

        # entry multiplicador
        borde_entry_2 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_2.grid(row=1, column=1, pady=(20, 0))

        self.multiplicador = tk.StringVar()
        tk.Entry(borde_entry_2,
                 textvariable=self.multiplicador,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, expand=True)

        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=200)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 200, 0, **style.STYLE_CANVAS_LINE)

        # label alerta multiplicador
        self.texto_alerta_multiplicador = tk.StringVar()
        tk.Label(borde_entry_2,
                 textvariable=self.texto_alerta_multiplicador,
                 **style.STYLE_WARNING
                 ).pack()

        # entry desactivado valor a_b
        borde_entry_3 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_3.grid(row=0, column=2)

        self.valor_a_b = tk.StringVar()
        tk.Entry(borde_entry_3,
                 textvariable=self.valor_a_b,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # entry desactivado valor c_d
        borde_entry_4 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_4.grid(row=1, column=2)

        self.valor_c_d = tk.StringVar()
        tk.Entry(borde_entry_4,
                 textvariable=self.valor_c_d,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.Y, expand=True)

        # entry desactivado formula
        borde_entry_5 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_5.grid(row=2, column=1, columnspan=2,
                           pady=(20, 0), sticky=tk.EW)

        self.valor_formula = tk.StringVar()
        tk.Entry(borde_entry_5,
                 textvariable=self.valor_formula,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas_linea_5 = tk.Canvas(
            borde_entry_5, **style.STYLE_CANVAS, width=500)
        canvas_linea_5.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_5.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado parte_1
        borde_entry_6 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_6.grid(row=3, column=1, columnspan=2,
                           pady=(20, 0), sticky=tk.EW)

        self.valor_parte_1 = tk.StringVar()
        tk.Entry(borde_entry_6,
                 textvariable=self.valor_parte_1,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas_linea_6 = tk.Canvas(
            borde_entry_6, **style.STYLE_CANVAS, width=500)
        canvas_linea_6.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_6.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado parte_2
        borde_entry_7 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_7.grid(row=4, column=1, columnspan=2,
                           pady=(20, 0), sticky=tk.EW)

        self.valor_parte_2 = tk.StringVar()
        tk.Entry(borde_entry_7,
                 textvariable=self.valor_parte_2,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas_linea_7 = tk.Canvas(
            borde_entry_7, **style.STYLE_CANVAS, width=500)
        canvas_linea_7.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_7.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado parte_3
        borde_entry_8 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_8.grid(row=5, column=1, columnspan=2,
                           pady=(20, 0), sticky=tk.EW)

        self.valor_parte_3 = tk.StringVar()
        tk.Entry(borde_entry_8,
                 textvariable=self.valor_parte_3,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas_linea_8 = tk.Canvas(
            borde_entry_8, **style.STYLE_CANVAS, width=500)
        canvas_linea_8.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_8.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # entry desactivado resultado
        borde_entry_9 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER,)
        borde_entry_9.grid(row=6, column=1, columnspan=2,
                           pady=(20, 0), sticky=tk.EW)

        self.valor_resultado = tk.StringVar()
        tk.Entry(borde_entry_9,
                 textvariable=self.valor_resultado,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas_linea_9 = tk.Canvas(
            borde_entry_9, **style.STYLE_CANVAS, width=500)
        canvas_linea_9.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_9.create_line(0, 0, 500, 0, **style.STYLE_CANVAS_LINE)

        # boton para calcular
        borde_1 = tk.LabelFrame(input_frame,
                                **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, column=3, pady=(30, 0), padx=20)

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.verificacion,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)
