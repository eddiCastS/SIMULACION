import pandas as pd
import random

# Generamos datos de dos grupos (tiempos de espera en minutos)
random.seed(42)
grupo_A = [random.randint(1, 10) for _ in range(15)]
grupo_B = [random.randint(1, 10) for _ in range(15)]

# Creamos DataFrame
df = pd.DataFrame({
    "Grupo": ["A"] * len(grupo_A) + ["B"] * len(grupo_B),
    "Tiempo": grupo_A + grupo_B
})

print("Datos:")
print(df)

# Calculamos la mediana global
mediana_global = df["Tiempo"].median()
print("\nMediana global:", mediana_global)

# Contamos cuántos valores de cada grupo están por encima y por debajo de la mediana
conteo = df.groupby("Grupo")["Tiempo"].apply(
    lambda x: {"menores": sum(v < mediana_global for v in x),
               "mayores": sum(v >= mediana_global for v in x)}
)

print("\nConteo de menores y mayores respecto a la mediana global:")
print(conteo)
