import random

def simulador(dias):
    inventario = 50
    for dia in range(dias):
        inventario -= random.randint(5, 15)
        if inventario < 20:
            inventario += 40
    return inventario


valor_real = 45
resultado_sim = simulador(10)
print(f"Resultado simulador: {resultado_sim}")
print(f"Diferencia con valor real: {abs(resultado_sim - valor_real)}")

if abs(resultado_sim - valor_real) < 5:
    print("Validación exitosa ")
else:
    print("Validación fallida")
