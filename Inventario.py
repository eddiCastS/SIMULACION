import pandas as pd
import numpy as np

np.random.seed(2025)
dias = 30
inv = 50
hist = []

for d in range(1, dias + 1):
    demanda = np.random.poisson(3)
    inv -= demanda
    if inv < 10:  # política de reorden
        inv += 40
    hist.append([d, demanda, inv])

df = pd.DataFrame(hist, columns=["Día", "Demanda", "Inventario"])
print(df)
print("\nInventario promedio:", df["Inventario"].mean())
