from pathlib import Path

import pandas as pd


def partial_to_full_path(path):
    parent = Path(__file__).parent
    for _ in range(path.count('../')):
        parent = parent.parent
    parent = str(parent)

    barras = path.count('../') * '../'
    parent += path[path.find(barras) + len(barras) - 1:]
    return parent


dados = pd.read_csv(partial_to_full_path("../csv/aluguel.csv"), sep=';')

print(dados)
