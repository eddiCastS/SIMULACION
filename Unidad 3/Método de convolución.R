poisson_convolucion <- function(lambda, n) {
  resultados <- numeric(n)
  for (j in 1:n) {
    L <- exp(-lambda)
    k <- 0
    p <- 1
    while (p > L) {
      k <- k + 1
      p <- p * runif(1)
    }
    resultados[j] <- k - 1
  }
  return(resultados)
}

poisson_convolucion(4, 10)
