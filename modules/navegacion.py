# Tema: Técnicas de diseño de algoritmos - Divide y Vencerás
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Carrera: Ingeniería en Sistemas de la Información
# Paralelo: SI4 - 002
# Fecha de entrega: 19/07/2023

import tkinter as tk
import functions.events as event
from static import style


class Navegacion (tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent
        self.init_widgets(parent)

    def colorear_boton(self):
        if self.ubicacion.get() == 1:
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_NORMAL,)
            self.boton_pi.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_karatsuba.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.boton_straws.configure(background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()
        elif self.ubicacion.get() == 2:
            self.boton_pi.configure(background=style.COLOR_MAGENTA_NORMAL)
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_karatsuba.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.boton_straws.configure(background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()
        elif self.ubicacion.get() == 3:
            self.boton_karatsuba.configure(
                background=style.COLOR_MAGENTA_NORMAL)
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_pi.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_straws.configure(background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()
        elif self.ubicacion.get() == 4:
            self.boton_straws.configure(background=style.COLOR_MAGENTA_NORMAL)
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_pi.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_karatsuba.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()

    def deshabilitar_eventos(self):
        if self.ubicacion.get() == 1:
            self.boton_inicio.bind('<Leave>', event.on_enter_nav)
            self.boton_pi.bind('<Leave>', event.on_leave_nav)
            self.boton_karatsuba.bind('<Leave>', event.on_leave_nav)
            self.boton_straws.bind('<Leave>', event.on_leave_nav)
        elif self.ubicacion.get() == 2:
            self.boton_pi.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio.bind('<Leave>', event.on_leave_nav)
            self.boton_karatsuba.bind('<Leave>', event.on_leave_nav)
            self.boton_straws.bind('<Leave>', event.on_leave_nav)
        elif self.ubicacion.get() == 3:
            self.boton_karatsuba.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio.bind('<Leave>', event.on_leave_nav)
            self.boton_pi.bind('<Leave>', event.on_leave_nav)
            self.boton_straws.bind('<Leave>', event.on_leave_nav)
        elif self.ubicacion.get() == 4:
            self.boton_straws.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio.bind('<Leave>', event.on_leave_nav)
            self.boton_pi.bind('<Leave>', event.on_leave_nav)
            self.boton_karatsuba.bind('<Leave>', event.on_leave_nav)

    def home(self):
        self.controller.move_to_home()
        self.ubicacion.set(value=1)
        self.colorear_boton()

    def pi(self):
        self.controller.move_to_pi()
        self.ubicacion.set(value=2)
        self.colorear_boton()

    def karatsuba(self):
        self.controller.move_to_karatsuba()
        self.ubicacion.set(value=3)
        self.colorear_boton()

    def strassen(self):
        self.controller.move_to_strassen()
        self.ubicacion.set(value=4)
        self.colorear_boton()

    def init_widgets(self, parent):
        nav_frame = tk.Frame(parent)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)
        nav_frame.configure(
            background=style.COLOR_MAGENTA_CLARO, borderwidth=0)

        self.ubicacion = tk.IntVar(value=1)
        self.boton_inicio = tk.Button(nav_frame,
                                      text="Inicio",
                                      **style.STYLE_BUTTON_NAV,
                                      command=self.home
                                      )
        self.boton_inicio.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.boton_inicio.config(background=style.COLOR_MAGENTA_NORMAL)
        self.boton_inicio.bind('<Enter>', event.on_enter_nav)

        self.boton_pi = tk.Button(nav_frame,
                                  text="Número Pi",
                                  **style.STYLE_BUTTON_NAV,
                                  command=self.pi
                                  )
        self.boton_pi.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.boton_pi.bind('<Enter>', event.on_enter_nav)
        self.boton_pi.bind('<Leave>', event.on_leave_nav)

        self.boton_karatsuba = tk.Button(nav_frame,
                                         text="Karatsuba",
                                         **style.STYLE_BUTTON_NAV,
                                         command=self.karatsuba
                                         )
        self.boton_karatsuba.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.boton_karatsuba.bind('<Enter>', event.on_enter_nav)
        self.boton_karatsuba.bind('<Leave>', event.on_leave_nav)

        self.boton_straws = tk.Button(nav_frame,
                                      text="Strassen",
                                      **style.STYLE_BUTTON_NAV,
                                      command=self.strassen
                                      )
        self.boton_straws.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.boton_straws.bind('<Enter>', event.on_enter_nav)
        self.boton_straws.bind('<Leave>', event.on_leave_nav)

        # label de información - footer
        tk.Label(nav_frame,
                 text="Técnicas de diseño\nDivide y Vencerás\nGrupo-3",
                 font=("Corbel", 10, "normal"),
                 background=style.COLOR_MAGENTA_CLARO,
                 foreground="#FFF",
                 justify="center"
                 ).pack(side=tk.BOTTOM, fill=tk.BOTH)
