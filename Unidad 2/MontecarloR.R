# Número de puntos
n <- 100000  

# Generar coordenadas aleatorias uniformes en [0,1]
x <- runif(n, 0, 1)
y <- runif(n, 0, 1)

# Contar cuántos puntos caen dentro del círculo de radio 1
dentro <- x^2 + y^2 <= 1  

# Aproximación de PI
pi_aprox <- 4 * sum(dentro) / n
print(pi_aprox)

# Graficar los puntos dentro del círculo (azules)
plot(x[dentro], y[dentro], col="blue", pch=16, cex=0.5,
     xlab="x", ylab="y", main="Método Monte Carlo para π")

# Graficar los puntos fuera del círculo (rojos)
points(x[!dentro], y[!dentro], col="red", pch=16, cex=0.5)

# Dibujar el cuarto de círculo real
theta <- seq(0, pi/2, length.out=500)
lines(cos(theta), sin(theta), col="black", lwd=2)
