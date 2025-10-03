n <- 10
valores <- numeric(n)
for (i in 1:n) {
  if (runif(1) < 0.5) {
    valores[i] <- rnorm(1, 0, 1)
  } else {
    valores[i] <- rexp(1, 1)
  }
}
valores
