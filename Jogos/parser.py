def getPalavras(path):
    palavras = []
    with open(path, 'r') as file:
        for linha in file:
            palavras.append(linha.strip("\n").upper())

    file.close()

    return palavras
