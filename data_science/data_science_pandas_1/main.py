import pandas as pd


def printa_linha_baseando_nome_carro(dataset):
    print(dataset.loc[['DS5'], ['Quilometragem']])  # printa uma tabela focando na quilometragem do DS5
    # .iloc vai pelo numero do indice
    # print(dataset.loc['DS5'])

    # loc = LINHA
    # dataset[x] = COLUNA


def printa_key_separada_do_value(dataset):
    for index, row in dict(dataset.head().iterrows()).items():
        print("\n", index, "\n")
        print(row)


def cria_coluna_km_media(dataset):
    for index, row in dataset.iterrows():
        if 2019 - row['Ano'] != 0:
            dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
        else:
            dataset.loc[index, 'Km_media'] = 0

    print(dataset)


def printa_apenas_colunas_atendendo_condicoes(dataset):
    # print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)])
    print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))


def mexe_com_nan(dataset):
    """ troca nan por 0"""

    # print(dataset[dataset.Quilometragem.isna()])
    dataset.fillna(0, inplace=True)  # substirui por 0 na dataset original, e nao retorna copia
    # print(dataset.query("Quilometragem == 0"))
    # print(dataset.query("Zero_km == True"))

    """ apaga nan"""
    dataset.dropna(subset=['Quilometragem'], inplace=True)


if __name__ == '__main__':
    pd.options.display.width = 320  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = 10  # pd.set_option('display.max_columns',10)

    dataset = pd.read_csv("data/db.csv", sep=';', index_col=0)

    print(dataset.loc[['DS5']])
