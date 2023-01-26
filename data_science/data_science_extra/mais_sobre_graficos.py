import matplotlib.pyplot as plt
import pandas as pd


def _4_graficos():
    dados = pd.read_csv('dados/aluguel.csv', sep=';')

    area = plt.figure()

    g1 = area.add_subplot(2, 2, 1)
    g2 = area.add_subplot(2, 2, 2)
    g3 = area.add_subplot(2, 2, 3)
    g4 = area.add_subplot(2, 2, 4)

    g1.scatter(dados['Valor'], dados['Area'])
    g1.set_title('Valor X Área')

    g2.hist(dados['Valor'])
    g2.set_title('Histograma')

    dados_g3 = dados['Valor'].sample(100)
    dados_g3.index = range(dados_g3.shape[0])
    g3.plot(dados_g3)
    g3.set_title('Amostra (Valor)')

    grupo = dados.groupby('Tipo')['Valor']
    label = grupo.mean().index
    valores = grupo.mean().values
    g4.bar(label, valores)
    g4.set_title('Valor Medio por tipo')

    area.savefig('dados/grafico.png', dpi=300, bbox_inches='tight')

    plt.show()


def grafico_pizza():

    dados = pd.read_csv('dados/aluguel_amostra.csv', sep=';')
    area = plt.figure()
    g1 = area.add_subplot(1, 2, 1)
    g2 = area.add_subplot(1, 2, 2)
    grupo1 = dados.groupby('Tipo Agregado')['Valor']
    label = grupo1.count().index
    valores = grupo1.count().values
    g1.pie(valores, labels=label, autopct='%1.1f%%')
    g1.set_title('Total de Imóveis por Tipo Agregado')
    grupo2 = dados.groupby('Tipo')['Valor']
    label = grupo2.count().index
    valores = grupo2.count().values
    g2.pie(valores, labels=label, autopct='%1.1f%%', explode=(.1, .1, .1, .1, .1))
    g2.set_title('Total de Imóveis por Tipo')
    plt.show()

if __name__ == '__main__':
    plt.rc('figure', figsize=(15, 8))

    pd.options.display.width = None
    pd.options.display.max_columns = None

    grafico_pizza()
