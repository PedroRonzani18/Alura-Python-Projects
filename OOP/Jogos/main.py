import  adivinhacao
import forca

if __name__ == '__main__':
    match int(input("1) Adivinhacao\n2) Forca\nEscolha: ")):
        case 1: adivinhacao.jogar()
        case 2: forca.jogar()