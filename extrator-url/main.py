from extrator_url import ExtratorURL

if __name__ == '__main__':
    extrator_url = ExtratorURL("bytebank.com/cambio?moedaOrigem=real")
    extrator_url2 = ExtratorURL("bytebank.com/cambio?moedaOrigem=real")
    print(f"URL: {extrator_url.url}\n")
    print(f"Bases: {extrator_url.base}\n")
    print(f"Parametros: {extrator_url.parametros}\n")
    print(f"moedaOrigem = {extrator_url.get_valor('moedaOrigem')}\n")
    print(extrator_url)
    print((extrator_url == extrator_url2))