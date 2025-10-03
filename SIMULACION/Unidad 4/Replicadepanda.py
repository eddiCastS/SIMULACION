import pandas as pd
import numpy as np


np.random.seed(42)
datos = {"Replica": [], "TiempoEspera": []}

for r in range(1, 11):
    tiempos = np.random.exponential(scale=5, size=20)
    for t in tiempos:
        datos["Replica"].append(r)
        datos["TiempoEspera"].append(t)

df = pd.DataFrame(datos)
print(df.head())


resumen = df.groupby("Replica")["TiempoEspera"].mean()
print("\nPromedio de cada réplica:")
print(resumen)
