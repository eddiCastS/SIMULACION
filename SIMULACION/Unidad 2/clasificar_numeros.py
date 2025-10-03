import random


numeros = [random.randint(-100, 100) for _ in range(10)]

print("Números generados:", numeros)


positivos = [n for n in numeros if n > 0]
negativos = [n for n in numeros if n < 0]


print("Positivos:", positivos)
print("Negativos:", negativos)
print("Cantidad de ceros:", numeros.count(0))
