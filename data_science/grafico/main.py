from matplotlib import pyplot
from random import randrange

notas_matematica = []

for notas in range(8):
    notas_matematica.append(randrange(0, 11))

x = list(range(1, 9))
y = notas_matematica

pyplot.plot(x, y, marker='o     ')
pyplot.title("Notas de Matematica")
pyplot.xlabel("Provas")
pyplot.ylabel("Notas")
pyplot.show()
