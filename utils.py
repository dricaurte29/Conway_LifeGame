import numpy as np
import pandas as pd




def suma_vecindad(m,fila, columna):
    vecindad = m[max(0, fila - 1):min(fila + 2, m.shape[0]),
                     max(0, columna - 1):min(columna + 2, m.shape[1])]
    return np.sum(vecindad) - m[fila, columna]
def generacion(m,SIZE):
    sumas_vecindad = np.zeros_like(m)
    for fila in range(m.shape[0]):
        for columna in range(m.shape[1]):
            sumas_vecindad[fila, columna] = suma_vecindad(m,fila, columna)
    for i in range(SIZE):
        for j in range(SIZE):
            if m[i,j] == 1:
                if sumas_vecindad[i,j] < 2:
                    m[i,j] = 0
                elif sumas_vecindad[i,j] > 3:
                    m[i,j] = 0
            else:
                if sumas_vecindad[i,j] == 3:
                    m[i,j] = 1     
    return m




