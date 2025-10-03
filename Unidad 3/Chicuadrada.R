datos <- runif(100)
conteos <- hist(datos, breaks=10, plot=FALSE)$counts
chisq.test(conteos, p=rep(1/10,10))
