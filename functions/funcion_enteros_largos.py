import tkinter as tk

def karatsuba_multiplicacion(x, y):
    if x < 10 or y < 10:
        return x * y

    m = max(len(str(x)), len(str(y)))
    m2 = m // 2

    a = x // 10**m2
    b = x % 10**m2
    c = y // 10**m2
    d = y % 10**m2

    ac = karatsuba_multiplicacion(a, c)
    bd = karatsuba_multiplicacion(b, d)
    ad_bc = karatsuba_multiplicacion(a + b, c + d) - ac - bd

    resultado = ac * 10**(2 * m2) + ad_bc * 10**m2 + bd
    return resultado

# def multiplicar():
#     try:
#         num1 = int(entry_num1.get())
#         num2 = int(entry_num2.get()
#         resultado = karatsuba_multiplicacion(num1, num2)
#         label_resultado.config(text=f"Resultado: {resultado}")
#     except ValueError:
#         label_resultado.config(text="Por favor, ingresa números enteros válidos.")

# # Configuración de la interfaz gráfica
# app = tk.Tk()
# app.title("Multiplicación con Karatsuba")
# app.geometry("400x200")

# label_num1 = tk.Label(app, text="Número 1:")
# label_num1.pack()
# entry_num1 = tk.Entry(app)
# entry_num1.pack()

# label_num2 = tk.Label(app, text="Número 2:")
# label_num2.pack()
# entry_num2 = tk.Entry(app)
# entry_num2.pack()

# btn_multiplicar = tk.Button(app, text="Multiplicar", command=multiplicar)
# btn_multiplicar.pack()

# label_resultado = tk.Label(app, font=("Arial", 14))
# label_resultado.pack(pady=20)

# app.mainloop()
