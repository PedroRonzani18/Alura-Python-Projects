import pandas as pd

if __name__ == '__main__':
    pd.options.display.width = None
    pd.options.display.max_columns = None
    dados = pd.read_csv('dados/aluguel.csv', sep=';')

    classes = [0, 2, 4, 6, 100]
    labels = ['1 e 2 quartos', '3 e  quartos', '5 e 6 quartos', '7 quartos ou mais']
    quartos = pd.cut(dados['Quartos'], classes)
    print(pd.value_counts(quartos))