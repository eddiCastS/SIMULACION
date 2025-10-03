import random


n = 1000000  
dentro_circulo = 0

for _ in range(n):
    x = random.random()  # número aleatorio entre 0 y 1
    y = random.random()
    
    
    if x*2 + y*2 <= 1:
        dentro_circulo += 1

pi_aprox = 4 * dentro_circulo / n
print("Aproximación de π:", pi_aprox)