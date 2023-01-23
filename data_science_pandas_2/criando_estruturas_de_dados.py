import pandas as pd


def criando_dataFrame_indices_strings():
    data = list(range(1, 6))
    s = pd.Series(data)
    index = ['Linha' + str(i) for i in range(5)]
    s = pd.Series(data=data, index=index)
    print(s)


def series():
    data = {'Linha' + str(i): i + 1 for i in range(5)}
    s = pd.Series(data)
    s1 = s + 2  # pode fazer operações aritmeticas
    print(s1)


def dataFrame():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df1 = pd.DataFrame(data)

    linhas =['Linha' + i for i in range(3)]
    colunas = ['Coluna' + i for i in range(3)]

    df1 = pd.DataFrame(data = data, index=linhas, columns=)


if __name__ == '__main__':
    dataFrame()
