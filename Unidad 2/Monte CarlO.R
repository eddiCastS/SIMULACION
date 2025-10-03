set.seed(123)
n <- 100000
x <- runif(n)
y <- runif(n)

dentro <- sum(x^2 + y^2 <= 1)
pi_aprox <- 4 * dentro / n

cat("Estimación de π con Monte Carlo:", pi_aprox, "\n")

# Opcional: Gráfico
plot(x, y, col = ifelse(x^2 + y^2 <= 1, "blue", "red"), pch=16, cex=0.3,
     main="Método Monte Carlo para π")
