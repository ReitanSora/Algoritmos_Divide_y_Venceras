from mpmath import mp
import tkinter as tk
from tkinter import ttk

def calcular_pi(decimales):
    mp.dps = decimales + 1  # Ajustamos la precisión a la cantidad de decimales deseados + 2

    # Inicialización de variables
    a = mp.mpf(1.0)
    b = mp.mpf(1.0) / mp.mpf(2).sqrt()
    t = mp.mpf(1.0) / mp.mpf(4)
    p = mp.mpf(1.0)

    # Iteraciones de la fórmula de Gauss-Legendre
    for _ in range(10):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next)**2
        a = a_next
        p *= 2

    # Aproximación final de π
    pi_value = (a + b)**2 / (4 * t)
    return pi_value

# def mostrar_pi():
#     decimales = int(combo_decimales.get())
#     pi = calcular_pi(decimales)
#     label_pi.config(text=f"π = {pi}")

# # Configuración de la interfaz gráfica
# app = tk.Tk()
# app.title("Número π (pi)")
# app.geometry("400x200")

# label_pi = tk.Label(app, font=("Arial", 14))
# label_pi.pack(pady=20)

# # Selección de decimales
# label_decimales = tk.Label(app, text="Selecciona la cantidad de decimales:")
# label_decimales.pack()

# decimales_disponibles = ["5", "10", "100", "500", "1000"]
# combo_decimales = ttk.Combobox(app, values=decimales_disponibles)
# combo_decimales.pack()


# btn_calcular = tk.Button(app, text="Calcular π", command=mostrar_pi)
# btn_calcular.pack()

# app.mainloop()
