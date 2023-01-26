import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    plt.rc('figure', figsize=(14, 16))

    pd.options.display.width = None
    pd.options.display.max_columns = None

    dados = pd.read_csv('csv/aluguel.residencial.csv', sep=';')

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

    dados_new.to_csv('csv/aluguel_residencial_sem_outliers.csv', sep=';', index=False)
