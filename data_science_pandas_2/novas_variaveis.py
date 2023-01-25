import pandas as pd


def adicionando_variaveis(dados):
    dados['Valor/m2'] = (dados['Valor'] / dados['Area']).round(2)
    dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']
    dados['Valor Bruto/m2'] = (dados['Valor Bruto'] / dados['Area']).round(2)

    casa = ['Casa', 'Casa de Condomínio', 'Casa de Vila']

    dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')


def removendo_variaveis(dados):
    dados.drop(['Valor Bruto/m2'], axis=1, inplace=True)


if __name__ == '__main__':
    pd.options.display.width = None  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = None  # pd.set_option('display.max_columns',10)

    dados = pd.read_csv('csv/aluguel.residencial.csv', sep=';')
    adicionando_variaveis(dados)
    removendo_variaveis(dados)

    dados.to_csv('csv/aluguel.residencial.csv', sep=';', index=False)
