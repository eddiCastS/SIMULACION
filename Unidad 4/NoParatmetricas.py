import numpy as np


np.random.seed(3)
grupoA = np.random.normal(50, 5, 10)
grupoB = np.random.normal(55, 5, 10)


datos = np.concatenate([grupoA, grupoB])
ranks = datos.argsort().argsort() + 1


n1, n2 = len(grupoA), len(grupoB)
R1 = np.sum(ranks[:n1])
U1 = R1 - n1*(n1+1)/2
U2 = n1*n2 - U1

print("U1 =", U1, " U2 =", U2)
