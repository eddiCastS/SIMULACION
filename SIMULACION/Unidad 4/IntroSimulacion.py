import pandas as pd


# Crear un DataFrame con tiempos de servicio ficticios
datos = {"Cliente": ["C1", "C2", "C3"],
"TiempoServicio": [5, 7, 4]}


df = pd.DataFrame(datos)
print("Datos de servicio:")
print(df)


# Calculamos sus estadísticas
print("\nEstadísticas:")
print(df["TiempoServicio"].describe())