import pandas as pd

""" Relatorio de Analise 1 """


def dataframe_tipos_imoveis_sem_duplicacao(df):
    tipo_de_imovel = df['Tipo'].drop_duplicates()
    tipo_de_imovel = pd.DataFrame(tipo_de_imovel)
    tipo_de_imovel.index = range(tipo_de_imovel.shape[0])
    tipo_de_imovel.columns.name = 'Id'
    print(tipo_de_imovel)


if __name__ == '__main__':
    pd.options.display.width = 320  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = 10  # pd.set_option('display.max_columns',10)

    df = pd.read_csv('csv/aluguel.csv', sep=';')  # ,index_col=0

    # df['Tipo'] = coluna de tipos ("array")
    # df['Tipo'][0] = array[0] (str)

    dataframe_tipos_imoveis_sem_duplicacao(df)
