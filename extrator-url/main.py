from extrator_url import ExtratorURL

if __name__ == '__main__':
    extrator_url = ExtratorURL("bytebank.com/cambio?moedaOrigem=real")
    print(extrator_url.getValor("moedaOrigem"))