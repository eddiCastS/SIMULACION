import random

n = 1000
numeros = [random.random() for _ in range(n)]


intervalos = [0]*10
for num in numeros:
    index = int(num*10)
    if index == 10: 
        index = 9
    intervalos[index] += 1

print("Frecuencia por intervalos (aprox. uniforme):")
for i, f in enumerate(intervalos):
    print(f"Intervalo {i/10:.1f} - {(i+1)/10:.1f}: {f}")
