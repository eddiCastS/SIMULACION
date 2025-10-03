set.seed(123)
n <- 100
numeros <- runif(n)

media <- mean(numeros)
num <- sum((numeros[1:(n-1)] - media) * (numeros[2:n] - media))
den <- sum((numeros - media)^2)

autocor <- num / den
cat("Autocorrelación entre consecutivos:", autocor, "\n")
