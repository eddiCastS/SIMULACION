import pandas as pd
import numpy as np

# Datos simulados de tiempos de espera
np.random.seed(1)
tiempos = np.random.normal(loc=20, scale=2, size=30)
df = pd.DataFrame({"Tiempo": tiempos})

print(df.describe())

# Prueba t manual: comparar con media teórica 20
mu_teorica = 20
media_muestral = df["Tiempo"].mean()
std_muestral = df["Tiempo"].std(ddof=1)  # ddof=1 para estimar la desviación estándar muestral
n = len(df)

t_stat = (media_muestral - mu_teorica) / (std_muestral / np.sqrt(n))

print(f"t={t_stat:.3f}")

