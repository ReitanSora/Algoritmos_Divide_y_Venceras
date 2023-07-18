# Tema: Técnicas de diseño de algoritmos - Divide y Vencerás
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Carrera: Ingeniería en Sistemas de la Información
# Paralelo: SI4 - 002
# Fecha de entrega: 19/07/2023

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
