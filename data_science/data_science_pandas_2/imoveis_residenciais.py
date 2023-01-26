import pandas as pd


def df_com_tipos_especificos():
    dados = pd.read_csv("csv/aluguel.csv", sep=';')

    residencial = list(dados['Tipo'].drop_duplicates())
    residencial = residencial[:5]

    print(dados)

    dados_residencial = dados[dados['Tipo'].isin(residencial)]
    dados_residencial.index = range(dados_residencial.shape[0])

    print(dados_residencial)

    dados_residencial.to_csv('csv/aluguel.residencial.csv', sep=';', index=False)


if __name__ == '__main__':
    pd.options.display.width = 320  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = 10  # pd.set_option('display.max_columns',10)

    df_com_tipos_especificos()
