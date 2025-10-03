import random


tiempo_total = 20   
tiempo = 0
cola = []
tiempo_cajero = 0
cliente_id = 0

print("Simulación de un cajero automático")
print("-----------------------------------")

while tiempo < tiempo_total:
    
    if random.random() < 0.5:
        cliente_id += 1
        cola.append(cliente_id)
        print(f"Minuto {tiempo}: Llega el Cliente {cliente_id} (cola = {len(cola)})")

    
    if tiempo_cajero == 0 and cola:
        cliente = cola.pop(0)
        tiempo_cajero = random.randint(2, 5)  
        print(f"Minuto {tiempo}: Cliente {cliente} empieza a usar el cajero (tarda {tiempo_cajero} min)")

    
    if tiempo_cajero > 0:
        tiempo_cajero -= 1
        if tiempo_cajero == 0:
            print(f"Minuto {tiempo}: El cliente termina su operación")

    
    tiempo += 1
