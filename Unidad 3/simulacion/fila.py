import numpy as np
import pandas as pd

# Parámetros de la simulación
np.random.seed(42)       # Para reproducibilidad
num_clientes = 15        # Número de clientes a simular
llegada_media = 5        # Tiempo medio entre llegadas
servicio_media = 4       # Tiempo medio de servicio

# Listas para almacenar datos
tiempos_llegada = []
tiempos_servicio = []
tiempos_inicio = []
tiempos_salida = []
tiempos_espera = []
tiempos_sistema = []

# Variables de control
tiempo_actual = 0
salida_anterior = 0

for i in range(num_clientes):
    # Tiempo entre llegadas (exponencial)
    inter_llegada = np.random.exponential(llegada_media)
    tiempo_actual += inter_llegada
    tiempos_llegada.append(round(tiempo_actual, 2))

    # Tiempo de servicio (exponencial)
    servicio = np.random.exponential(servicio_media)
    tiempos_servicio.append(round(servicio, 2))

    # El inicio del servicio es cuando llega el cliente o cuando termina el anterior
    inicio = max(tiempo_actual, salida_anterior)
    tiempos_inicio.append(round(inicio, 2))

    # Tiempo de salida
    salida = inicio + servicio
    tiempos_salida.append(round(salida, 2))

    # Calcular métricas
    espera = inicio - tiempo_actual
    sistema = salida - tiempo_actual

    tiempos_espera.append(round(espera, 2))
    tiempos_sistema.append(round(sistema, 2))

    # Actualizar para el siguiente
    salida_anterior = salida

# Crear DataFrame
df = pd.DataFrame({
    "Cliente": range(1, num_clientes + 1),
    "Llegada": tiempos_llegada,
    "Servicio": tiempos_servicio,
    "Inicio_Servicio": tiempos_inicio,
    "Salida": tiempos_salida,
    "Espera": tiempos_espera,
    "Tiempo_en_Sistema": tiempos_sistema
})

print(df)

# Mostrar estadísticas
print("\n--- Estadísticas ---")
print("Promedio de espera:", round(df["Espera"].mean(), 2))
print("Promedio en el sistema:", round(df["Tiempo_en_Sistema"].mean(), 2))
