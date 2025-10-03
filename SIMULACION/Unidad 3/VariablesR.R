#  Variable aleatoria discreta: Binomial
discreta <- rbinom(10, size=10, prob=0.5)
print("Variable discreta (Binomial):")
print(discreta)

#  Variable aleatoria continua: Exponencial usando transformada inversa
U <- runif(10)
lambda <- 1.5
continua <- -log(U)/lambda
print("Variable continua (Exponencial por transformada inversa):")
print(continua)

#  Frecuencia de valores discretos
frecuencia <- table(discreta)
print("Frecuencia de valores discretos:")
print(frecuencia)
