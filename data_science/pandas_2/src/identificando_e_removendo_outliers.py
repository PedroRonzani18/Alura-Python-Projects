from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def partial_to_full_path(path):
    parent = Path(__file__).parent
    for _ in range(path.count('../')):
        parent = parent.parent
    parent = str(parent)

    barras = path.count('../') * '../'
    parent += path[path.find(barras) + len(barras) - 1:]
    return parent


def remove_outliers(dados):
    valor = dados['Valor']

    Q1 = valor.quantile(.25)
    Q3 = valor.quantile(.75)
    IIQ = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IIQ
    limite_superior = Q3 + 1.5 * IIQ

    selecao = (limite_inferior <= valor) & (valor <= limite_superior)

    dados_new = dados[selecao]
    # dados_new.boxplot(['Valor'])

    grupo_tipo = dados.groupby('Tipo')['Valor']

    Q1 = grupo_tipo.quantile(.25)
    Q3 = grupo_tipo.quantile(.75)
    IIQ = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IIQ
    limite_superior = Q3 + 1.5 * IIQ

    dados_new = pd.DataFrame()

    for tipo in grupo_tipo.groups.keys():
        eh_tipo = dados['Tipo'] == tipo
        eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
        selecao = eh_tipo & eh_dentro_limite
        dados_new = pd.concat([dados_new, dados[selecao]])

    dados_new.boxplot(['Valor'], by=['Tipo'])

    return_file = Path(__file__).parent.parent / "csv" / 'aluguel_residencial_sem_outliers.csv'
    dados_new.to_csv(return_file, sep=';', index=False)


if __name__ == '__main__':
    plt.rc('figure', figsize=(14, 16))

    pd.options.display.width = None
    pd.options.display.max_columns = None

    csv_file = Path(__file__).parent.parent / "csv" / "aluguel.residencial.csv"
    dados = pd.read_csv(partial_to_full_path("../csv/aluguel.residencial.csv"), sep=';')

    remove_outliers(dados)
