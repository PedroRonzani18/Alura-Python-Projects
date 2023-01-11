def cabecalho(msg):
    print((len(msg)+4)* "*")
    print(f"* {msg} *")
    print((len(msg)+4)* "*")


def printElements(elements,spacing=False, ending=""):
    for i in elements:
        print(i, end="")
        if(spacing == True):
            print(" ", end="")
    print(f"{ending}", end="")