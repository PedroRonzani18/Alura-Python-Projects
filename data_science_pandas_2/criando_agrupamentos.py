import pandas as pd

if __name__ == '__main__':
    pd.options.display.width = 30  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = 30  # pd.set_option('display.max_columns',10)

    dados = pd.read_csv('csv/aluguel.residencial.csv', sep=';')

    bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
    selecao = dados['Bairro'].isin(bairros)
    dados = dados[selecao]

    grupo_bairro = dados.groupby('Bairro')

    print(grupo_bairro.groups)

    for bairro, dados in grupo_bairro:
       print(f'{bairro} -> {dados}')