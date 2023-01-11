import interface


def alteraHiding(palavra, hiding, letra):
    for i in range(len(palavra)):
        if palavra[i] == letra:
            hiding[2 * i] = letra


def jogar():
    palavra = "BANANA"
    hiding = []
    erros = []
    vidas = 5

    for i in palavra:
        hiding.append("_")
        hiding.append(" ")

    win = False
    lose = False

    while not (win or lose):

        print(f"\nVidas restantes: {vidas}")
        interface.printElements(hiding,False,":")

        chute = str(input()).upper()

        if chute in palavra:
            alteraHiding(palavra, hiding, chute)

        else:
            if chute not in erros:
                erros.append(chute)
            vidas -= 1

        if "_" not in hiding: win = True

        if vidas == 0: lose = True

        print("Erros: ", end="")
        interface.printElements(erros,True," ")
        print()

    if win:
        print("\nVITORIA!!!")
    elif lose:
        print(f"\nDerrota. A palavra era {palavra}")
