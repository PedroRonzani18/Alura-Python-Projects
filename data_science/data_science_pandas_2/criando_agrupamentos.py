import matplotlib.pyplot as plt
import pandas as pd


def agurpando_por_nome_bairro(dados):
    bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca']
    selecao = dados['Bairro'].isin(bairros)
    dados = dados[selecao]


    grupo_bairro = dados.groupby('Bairro')

    # for bairro, dados in grupo_bairro:
    #  print(f'{bairro} -> {dados[["Valor"]].mean()}')

    # print(grupo_bairro['Valor'].describe().round(2)) # mostra varios dados estatisticos  associados aos valores de cada bairro

    # print(grupo_bairro['Valor'].aggregate(['min', 'max', 'sum']).rename(columns={'min': 'Minimo'}))
    fig = grupo_bairro['Valor'].std().plot.bar(color='red')
    fig.set_ylabel('Valor do Aluguel')
    fig.set_title('Valor Medio do Aluguel do Bairro', {'fontsize': 22})
    plt.show()


def notas_medias_por_sexo():
    alunos = pd.DataFrame({'Nome': ['Ary', 'Cátia', 'Denis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'],
                           'Sexo': ['M', 'F', 'M', 'M', 'F', 'F', 'M', 'F'],
                           'Idade': [15, 27, 56, 32, 42, 21, 19, 35],
                           'Notas': [7.5, 2.5, 5.0, 10, 8.2, 7, 6, 5.6],
                           'Aprovado': [True, False, False, True, True, True, False, False]},
                          columns=['Nome', 'Idade', 'Sexo', 'Notas', 'Aprovado'])

    sexo = alunos.groupby('Sexo')
    sexo = pd.DataFrame(sexo['Notas'].mean().round(2))
    sexo.columns = ['Notas Médias']
    print(sexo)


if __name__ == '__main__':
    pd.options.display.width = None  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = None  # pd.set_option('display.max_columns',10)
    plt.rc('figure', figsize=(20, 10))

    dados = pd.read_csv('csv/aluguel.residencial.csv', sep=';')

    # agurpando_por_nome_bairro(dados)
    notas_medias_por_sexo()
