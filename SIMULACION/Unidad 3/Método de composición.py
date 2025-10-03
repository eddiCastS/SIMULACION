import numpy as np

n = 18
valores = []
for _ in range(n):
    if np.random.rand() < 0.5:
        valores.append(np.random.normal(0,1))
    else:
        valores.append(np.random.exponential(1))
print(valores)
