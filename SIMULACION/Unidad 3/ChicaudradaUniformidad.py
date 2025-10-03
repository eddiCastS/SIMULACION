import numpy as np


datos = np.random.rand(100)
conteos, _ = np.histogram(datos, bins=12)
esperado = len(datos) / 12
chi2 = np.sum((conteos - esperado) ** 2 / esperado)
print("Chi-cuadrada calculada manualmente:", chi2)
