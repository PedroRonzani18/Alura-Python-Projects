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


def remove_todos_nulos(dados):
    # dados.isnull() # contrario: notnull()

    print(dados)

    A = dados.shape[0]
    # dados.dropna(subset = ['Valor'], inplace = True)
    dados.dropna(inplace=True)
    B = dados.shape[0]

    dados.index = range(dados.shape[0])

    print(A - B)
    print(dados)


def remocao_seletiva(dados):
    # 1) Elimina os registros que não apresentam a variável Valor
    dados.dropna(subset=['Valor'], inplace=True)

    # 2) Elimina os imóveis do tipo Apartamento que não apresentam valor Condominio
    selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())  # seleciona quem retirar
    dados = dados[~selecao]  # pega todos fora da

    # 3) Substitui os valores faltantes que restam nas variáveis Condominio e IPTU por zero:
    """ 
    dados['Condominio'].fillna(0, inplace=True)
    dados['IPTU'].fillna(0, inplace=True)
    """
    dados = dados.fillna({'Condominio': 0, 'IPTU': 0})

    # 4) Reconstrói o índice do DataFrame resultante:
    dados.index = range(dados.shape[0])

    # print(dados[dados['Condominio'].isnull()].shape[0])
    # print(dados[dados['IPTU'].isnull()].shape[0])

    dados.to_csv(partial_to_full_path('../csv/aluguel.residencial.csv'), sep=';', index=False)


if __name__ == '__main__':
    pd.options.display.width = 320  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = 10  # pd.set_option('display.max_columns',10)

    dados = pd.read_csv(partial_to_full_path('../csv/aluguel.residencial.csv'), sep=';')

    print(dados)
    remocao_seletiva(dados)
    print(pd.read_csv(partial_to_full_path('../csv/aluguel.residencial.csv'), sep=';'))
