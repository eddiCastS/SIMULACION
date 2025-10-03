rtriangular <- function(n, a, b, c) {
  u <- runif(n)
  f <- (c - a) / (b - a)
  x <- ifelse(u < f, a + sqrt(u * (b - a) * (c - a)),
              b - sqrt((1 - u) * (b - a) * (b - c)))
  return(x)
}

rtriangular(10, 0, 10, 5)
