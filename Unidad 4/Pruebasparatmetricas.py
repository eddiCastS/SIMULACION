import numpy as np

# Generar datos simulados
np.random.seed(1)
datos = np.random.normal(loc=50, scale=5, size=30)

# Parámetros
media_muestral = np.mean(datos)
media_hipotesis = 50
desv_estandar = np.std(datos, ddof=1)  # ddof=1 para desviación muestral
n = len(datos)

# Cálculo de t
t_stat = (media_muestral - media_hipotesis) / (desv_estandar / np.sqrt(n))

print("Media de los datos:", media_muestral)
print("Estadístico t:", t_stat)

# Como no usamos scipy, solo interpretamos con regla básica
print("\nInterpretación:")
print("- Si |t| < 2 → no hay diferencia significativa (p > 0.05).")
print("- Si |t| >= 2 → diferencia significativa (p < 0.05).")
