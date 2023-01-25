import pandas as pd


def dataFrame():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    linhas = ['Linha' + str(i) for i in range(3)]
    colunas = ['Coluna' + str(i) for i in range(3)]

    df1 = pd.DataFrame(data=data, index=linhas, columns=colunas)

    # print(df1)

    data2 = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
             'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
             'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}

    df2 = pd.DataFrame(data2)

    # print(df2)

    data = [(1, 2, 3),(4, 5, 6),(7, 8, 9)]

    df3 = pd.DataFrame(data)

    df1[df1 > 0] = 'A'
    df2[df2 > 0] = 'B'
    df3[df3 > 0] = 'C'

    df4 = pd.concat([df1, df2, df3], axis=0)  # tabela vertical
    df4 = pd.concat([df1, df2, df3], axis=1)  # tabela horizontal

    print(df4)


if __name__ == "__main__":
    dados = [('A', 'B'), ('C', 'D')]
    df = pd.DataFrame(dados, columns=['L1', 'L2'], index=['C1', 'C2'])
    print(df)
