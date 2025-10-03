import numpy as np


discreta = np.random.binomial(n=10, p=0.5, size=10)
print("Variable discreta (Binomial):", discreta)


U = np.random.uniform(0,1,10)
lambd = 1.5
continua = -np.log(U)/lambd
print("Variable continua (Exponencial por transformada inversa):", continua)

frecuencia = np.bincount(discreta)
print("Frecuencia de valores discretos:", frecuencia)
