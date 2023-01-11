import interface
import parser
from random import  randint


def palavraSecreta():
    dados = parser.getPalavras("palavras.txt")
    return dados[randint(0, len(dados))]


def maximum():
    while (True):
        dificuldade = int(input("Nivel de dificuldade (1)Facil (2)Medio (3)Dificil: "))
        if (dificuldade in (1,2,3)):
            break
        else:
            print("Valor inválido\n")

    match dificuldade:
        case 1: return 15
        case 2: return 10
        case 3: return 5


def alteraHiding(palavra, hiding, letra):
    for i in range(len(palavra)):
        if palavra[i] == letra:
            hiding[2 * i] = letra


def loadHiding(palavra):
    hiding = []
    for i in palavra:
        hiding.append("_")
        hiding.append(" ")
    hiding.pop()

    return hiding

def jogar():

    win = False
    lose = False
    erros = []

    vidas = maximum()
    palavra = palavraSecreta()
    hiding = loadHiding(palavra)

    interface.cabecalho("BEM VINDO AO JOGO DA FORCA")

    while not (win or lose):

        print(f"\nVidas restantes: {vidas}")
        interface.printElements(hiding,False,": ")

        chute = str(input()).strip().upper()

        if chute in palavra:
            alteraHiding(palavra, hiding, chute)

        else:
            if chute not in erros:
                erros.append(chute)
            vidas -= 1

        win = "_" not in hiding
        lose = vidas == 0

        print("Erros: ", end="")
        interface.printElements(erros,True," ")
        print()

    if win:
        print("\nVITORIA!!!")
    elif lose:
        print(f"\nDerrota. A palavra era {palavra}")
