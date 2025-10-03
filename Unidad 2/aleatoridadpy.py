import random


n = 100
numeros = [random.random() for _ in range(n)]


media = sum(numeros)/len(numeros)
binario = [1 if x > media else 0 for x in numeros]


runs = 1
for i in range(1, len(binario)):
    if binario[i] != binario[i-1]:
        runs += 1

print("Número de runs:", runs)
print("Longitud de secuencia:", len(binario))
