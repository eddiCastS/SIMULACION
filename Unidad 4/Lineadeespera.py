import random

# Parámetros de la simulación
tiempo_total = 30   # Minutos de simulación
tiempo = 0
cola = []
tiempos_cajeros = [0, 0]  # Dos cajeros disponibles
cliente_id = 0

print("Simulación de un banco con 2 cajeros")
print("------------------------------------")

while tiempo < tiempo_total:
    # Probabilidad de llegada de un cliente por minuto (60%)
    if random.random() < 0.6:
        cliente_id += 1
        cola.append(cliente_id)
        print(f"Minuto {tiempo}: Llega el Cliente {cliente_id} (cola = {len(cola)})")

    # Revisar cada cajero
    for i in range(len(tiempos_cajeros)):
        if tiempos_cajeros[i] == 0 and cola:  # Cajero libre y hay clientes esperando
            cliente = cola.pop(0)
            tiempos_cajeros[i] = random.randint(3, 6)  # Tiempo de servicio
            print(f"Minuto {tiempo}: Cliente {cliente} empieza en Cajero {i+1} (tarda {tiempos_cajeros[i]} min)")

        # Avanzar servicio si está ocupado
        if tiempos_cajeros[i] > 0:
            tiempos_cajeros[i] -= 1
            if tiempos_cajeros[i] == 0:
                print(f"Minuto {tiempo}: El Cajero {i+1} termina con un cliente")

    # Avanza el tiempo
    tiempo += 1
