import pandas as pd


def contagem_moedas():
    m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
    m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
    m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
    m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
    m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'

    eventos = {'m1': list(m1),
               'm2': list(m2),
               'm3': list(m3),
               'm4': list(m4),
               'm5': list(m5)}
    moedas = pd.DataFrame(eventos)

    df = pd.DataFrame(data=['Cara', 'Coroa'],
                      index=['c', 'C'],
                      columns=['Faces'])

    for item in moedas:
        print(moedas[item])
        df = pd.concat([df, moedas[item].value_counts()], axis=1)


s = pd.Series(list('asdasdasdasdsadasdsdasdassddsadasaddsdasd'))
dados = pd.read_csv('dados/aluguel.csv', sep=';')
print(dados['Tipo'].unique())
