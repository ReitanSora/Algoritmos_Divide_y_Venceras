import tkinter as tk
import numpy as np

MAX_DIMENSION = 120


def division_matriz(matriz):
    # row, col = matriz.shape
    # row2, col2 = row//2, col//2
    # return matriz[:row2, :col2], matriz[:row2, col2:], matriz[row2:, :col2], matriz[row2:, col2:]

    size = matriz.shape[0]//2
    return matriz[:size, :size], matriz[:size, size:], matriz[size:, :size], matriz[size:, size:]

def _mat_mul_2x2(M, N):
    """Multiply two 2-by-2 matrices.
    """
    return np.array([[M[0][0] * N[0][0] + M[0][1] * N[1][0], 
                      M[0][0] * N[0][1] + M[0][1] * N[1][1]], 
                     [M[1][0] * N[0][0] + M[1][1] * N[1][0],
                      M[1][0] * N[0][1] + M[1][1] * N[1][1]]])

def strassen_multiplicacion(x, y):
    n = len(x)

    if x.shape[1] != y.shape[0]:
        pass
        #raise Exception("Inconsistent shape for Strassen Algorithm")
    max_size = max(np.amax(x.shape), np.amax(y.shape))
    if max_size == 0:
        return np.array([[]])
    elif max_size == 1:
        return np.array([[x[0][0] * y[0][0]]])
    square_size = (int)(np.exp2(np.ceil(np.log2(max_size))))

    if x.shape[0] == x.shape[1] == y.shape[0] == y.shape[1] == 2:
        return _mat_mul_2x2(x, y)

    # if n == 1:
    #     return np.dot(x,y)

    # if n <= MAX_DIMENSION:
    #     # Utilizar el método de multiplicación estándar para matrices pequeñas
    #     return np.dot(x, y)

    # m = n // 2
    # a, b = x[:m, :m], x[:m, m:]
    # c, d = x[m:, :m], x[m:, m:]
    # e, f = y[:m, :m], y[:m, m:]
    # g, h = y[m:, :m], y[m:, m:]

    a, b, c, d =  division_matriz(x)
    e, f, g, h = division_matriz(y)

    p1 = strassen_multiplicacion(a, f - h)
    p2 = strassen_multiplicacion(a + b, h)
    p3 = strassen_multiplicacion(c + d, e)
    p4 = strassen_multiplicacion(d, g - e)
    p5 = strassen_multiplicacion(a + d, e + h)
    p6 = strassen_multiplicacion(b - d, g + h)
    p7 = strassen_multiplicacion(a - c, e + f)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    resultado = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    # resultado = []
    # for i in range(n):
    #     resultado.append([])
    #     for j in range(n):
    #         resultado[i].append()

    return resultado

# def generar_matrices():
#     try:
#         dimension = int(entry_dimension.get())
#         if dimension <= 0 or dimension > MAX_DIMENSION:
#             label_resultado.config(text=f"Ingresa una dimensión válida (1 a {MAX_DIMENSION}).")
#             label_matrices.config(text="")
#             return

#         matriz1 = np.random.randint(1, 10, size=(dimension, dimension))
#         matriz2 = np.random.randint(1, 10, size=(dimension, dimension))

#         resultado = strassen_multiplicacion(matriz1, matriz2)

#         label_matrices.config(text=f"Matriz A:\n{matriz1}\n\nMatriz B:\n{matriz2}")
#         label_resultado.config(text=f"Resultado:\n{resultado}")
#     except ValueError:
#         label_resultado.config(text="Por favor, ingresa una dimensión válida.")
#         label_matrices.config(text="")

# # Configuración de la interfaz gráfica
# app = tk.Tk()
# app.title("Multiplicación de Matrices con Strassen")
# app.geometry("400x400")

# label_dimension = tk.Label(app, text=f"Ingresa la dimensión de las matrices (1 a {MAX_DIMENSION}):")
# label_dimension.pack()
# entry_dimension = tk.Entry(app)
# entry_dimension.pack()

# btn_generar = tk.Button(app, text="Generar y Multiplicar", command=generar_matrices)
# btn_generar.pack()

# label_matrices = tk.Label(app, font=("Arial", 10), justify="left")
# label_matrices.pack(pady=20)

# label_resultado = tk.Label(app, font=("Arial", 10), justify="left")
# label_resultado.pack(pady=20)

# app.mainloop()
