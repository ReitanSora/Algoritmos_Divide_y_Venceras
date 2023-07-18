# Tema: Técnicas de diseño de algoritmos - Divide y Vencerás
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Carrera: Ingeniería en Sistemas de la Información
# Paralelo: SI4 - 002
# Fecha de entrega: 19/07/2023

from mpmath import mp

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
