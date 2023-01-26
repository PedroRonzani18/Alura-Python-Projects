import pandas as pd

if __name__ == '__main__':
    pd.options.display.width = 320  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = None  # pd.set_option('display.max_columns',10)
    dados = pd.read_csv('csv/aluguel.residencial.csv', sep=';')

    print(dados)

    # Selecione somente os imóveis classificados com tipo 'Apartamento'.
    selecao = dados['Tipo'] == 'Apartamento'
    n1 = dados[selecao].shape[0]

    # Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
    selecao = dados['Tipo'].isin(['Casa', 'Casa de Condomínio', 'Casa de Vila'])
    n2 = dados[selecao].shape[0]

    # Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
    selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
    n3 = dados[selecao].shape[0]

    # Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
    selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
    n4 = dados[selecao].shape[0]

    print(f"Nº de imóveis classificados com tipo 'Apartamento' -> {n1}")
    print(f"Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'-> {n2}")
    print(f"Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {n3}")
    print(f"Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {n4}")
