import pandas as pd

if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    df = pd.DataFrame(data, list('321'), list('ZYX'))
    df.sort_index(inplace=True, axis=0)  # sort linhas
    df.sort_index(inplace=True, axis=1)  # sort colunas
    df.sort_values(inplace=True, by='X')  # sort coluna 'X'

    print(df)
