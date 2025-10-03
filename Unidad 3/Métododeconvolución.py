import numpy as np

def poisson_convolucion(lmbda, n):
    resultados = []
    for _ in range(n):
        L = np.exp(-lmbda)
        k = 0
        p = 1.0
        while p > L:
            k += 1
            p *= np.random.rand()
        resultados.append(k-1)
    return resultados

print(poisson_convolucion(4, 13))
