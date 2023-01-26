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


if __name__ == '__main__':
    series()