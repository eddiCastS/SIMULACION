# Número decimal aleatorio entre -1000 y 1000
numero_decimal <- runif(1, min = -1000, max = 1000)
print(numero_decimal)

# Número entero aleatorio entre -1000 y 1000
numero_entero <- sample(-1000:1000, 1)
print(numero_entero)

# Número normal aleatorio (media 0, desviación 300)
numero_normal <- rnorm(1, mean = 0, sd = 300)
print(numero_normal)
