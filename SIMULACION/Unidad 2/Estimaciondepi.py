import random
import matplotlib.pyplot as plt

n = 100000
dentro = 0
x_vals = []
y_vals = []

for _ in range(n):
    x = random.random()
    y = random.random()
    x_vals.append(x)
    y_vals.append(y)
    if x**2 + y**2 <= 1: dentro += 1

pi_aprox = 4 * dentro / n
print("Estimación de π:", pi_aprox)
plt.scatter(x_vals, y_vals, c=['blue' if xi**2 + yi**2 <= 1 else 'red' for xi, yi in zip(x_vals, y_vals)], s=1)
plt.show()
