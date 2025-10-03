import random

inventario = 50

for dia in range(1, 11):
    inventario -= random.randint(5, 15)
    if inventario < 20: inventario += 40
    print(f"Día {dia}: Inventario = {inventario}")
