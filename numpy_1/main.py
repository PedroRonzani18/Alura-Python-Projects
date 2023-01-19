import numpy as np

km = np.loadtxt(fname="data/carros-km.txt", dtype=int)
anos = np.loadtxt(fname="data/carros-anos.txt", dtype=int)
valor = np.loadtxt(fname="data/carros-valor.txt")

media = km / (2023 - anos)

print(km)