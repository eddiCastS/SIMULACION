set.seed(123)
n <- 1000
numeros <- runif(n)

# Dividir en 10 intervalos
intervalos <- cut(numeros, breaks=seq(0,1,0.1), include.lowest=TRUE)
tabla <- table(intervalos)

print("Frecuencia por intervalos (aprox. uniforme):")
print(tabla)

# Opcional: Histograma
hist(numeros, breaks=10, col="skyblue", main="Prueba de uniformidad", xlab="Valor")
