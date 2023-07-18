# Tema: Técnicas de diseño de algoritmos - Divide y Vencerás
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Carrera: Ingeniería en Sistemas de la Información
# Paralelo: SI4 - 002
# Fecha de entrega: 19/07/2023

import numpy as np


def _pad(M, size):
    """Add zeros to turn matrix M into a squre matrix of shape (size, size).
    """
    M_pad = np.zeros((size, size))
    M_pad[: M.shape[0], : M.shape[1]] = M
    return M_pad


def _partition(M):
    """Evenly partition a matrix into 4 blocks (2-by-2).
    """
    block_size = M.shape[0] // 2
    M_11 = M[: block_size, : block_size]
    M_12 = M[: block_size, block_size:]
    M_21 = M[block_size:, : block_size]
    M_22 = M[block_size:, block_size:]
    return (M_11, M_12, M_21, M_22)


def _mat_mul_2x2(M, N):
    """Multiply two 2-by-2 matrices.
    """
    return np.array([[M[0][0] * N[0][0] + M[0][1] * N[1][0],
                      M[0][0] * N[0][1] + M[0][1] * N[1][1]],
                     [M[1][0] * N[0][0] + M[1][1] * N[1][0],
                      M[1][0] * N[0][1] + M[1][1] * N[1][1]]])


def _iterate(A, B):
    """The iterate process of the Strassen algorithm.
    """
    if A.shape[0] == A.shape[1] == B.shape[0] == B.shape[1] == 2:
        return _mat_mul_2x2(A, B)

    A_11, A_12, A_21, A_22 = _partition(A)
    B_11, B_12, B_21, B_22 = _partition(B)

    M_1 = _iterate(A_11 + A_22, B_11 + B_22)
    M_2 = _iterate(A_21 + A_22, B_11)
    M_3 = _iterate(A_11, B_12 - B_22)
    M_4 = _iterate(A_22, B_21 - B_11)
    M_5 = _iterate(A_11 + A_12, B_22)
    M_6 = _iterate(A_21 - A_11, B_11 + B_12)
    M_7 = _iterate(A_12 - A_22, B_21 + B_22)

    C = np.zeros(A.shape)
    block_size = C.shape[0] // 2
    C[: block_size, : block_size] = M_1 + M_4 - M_5 + M_7
    C[: block_size, block_size:] = M_3 + M_5
    C[block_size:, : block_size] = M_2 + M_4
    C[block_size:, block_size:] = M_1 - M_2 + M_3 + M_6

    return C


def strassen(X, Y):
    """The user interface of the Strassen algorithm.
    """
    if X.shape[1] != Y.shape[0]:
        raise Exception("Inconsistent shape for Strassen Algorithm")
    max_size = max(np.amax(X.shape), np.amax(Y.shape))
    if max_size == 0:
        return np.array([[]])
    elif max_size == 1:
        return np.array([[X[0][0] * Y[0][0]]])
    square_size = (int)(np.exp2(np.ceil(np.log2(max_size))))

    A = _pad(X, square_size)
    B = _pad(Y, square_size)

    C = _iterate(A, B)

    return C[: X.shape[0], : Y.shape[1]]


def generar_matrices(dimension):
    return np.random.randint(1, 11, (dimension, dimension))