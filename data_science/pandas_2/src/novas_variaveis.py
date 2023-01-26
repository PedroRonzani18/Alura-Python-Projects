import pandas as pd


def partial_to_full_path(path):
    from pathlib import Path

    parent = Path(__file__).parent
    for _ in range(path.count('../')):
        parent = parent.parent
    parent = str(parent)

    barras = path.count('../') * '../'
    parent += path[path.find(barras) + len(barras) - 1:]
    return parent


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

    dados = pd.read_csv(partial_to_full_path('../csv/aluguel.residencial.csv'), sep=';')
    adicionando_variaveis(dados)
    removendo_variaveis(dados)

    dados.to_csv(partial_to_full_path('../csv/aluguel.residencial.csv'), sep=';', index=False)
