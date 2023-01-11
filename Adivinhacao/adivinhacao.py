import random
import math

def maximum():
    while (True):
        dificuldade = int(input("Nivel de dificuldade (1)Facil (2)Medio (3)Dificil: "))
        if (dificuldade in (1,2,3)):
            break
        else:
            print("Valor inválido\n")

    match dificuldade:
        case 1: return 20
        case 2: return 15
        case 3: return 10


def jogoAdivinhacao():
    maximoTentativas = maximum()
    segredo = random.randint(1, 100)
    pontos = 1000

    for rodada in range(0, maximoTentativas):
        if (rodada == maximoTentativas): break

        while (True):
            chute = int(input(f"\n[Tentativa {rodada + 1}] Digite um numero entre 1 e 100: "))
            if (1 <= chute and chute <= 100): break
            else: print("Numero Invalido, digite novamente.")

        if (chute == segredo):
            print(f"\nVITORIA!! Pontuacao: {pontos}")
            exit()

        if (chute < segredo):
            print("O segredo é MAIOR")
        elif (chute > segredo):
            print("O segredo é MENOR")

        pontos -= abs(segredo - chute)

    print(f"Você perdeu. O segredo era {segredo}")
