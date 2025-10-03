set.seed(123)
n <- 100
numeros <- runif(n)

media <- mean(numeros)
binario <- ifelse(numeros > media, 1, 0)

runs <- 1
for (i in 2:length(binario)) {
  if (binario[i] != binario[i-1]) {
    runs <- runs + 1
  }
}

cat("Número de runs:", runs, "\n")
cat("Longitud de secuencia:", length(binario), "\n")
