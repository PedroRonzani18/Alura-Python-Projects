import re


class ExtratorURL:
    def __init__(self, url):
        self.__url = url
        self.__map = {}

        self.__loadURL(url)
        self.__loadValues()

    def __str__(self):
        retorno = "Conteudo do Extrator:\n"
        for k, v in self.__map.items():
            retorno += f"   {k} = {v}"
        return retorno

    def __len__(self):
        return len(self.__url)

    def __eq__(self, other):
        return self.__url == other.url

    def __valida_url(self):
        padrao_url = re.compile("(https://)?(www.)?bytebank.com(.br)?/cambio")

        if padrao_url.match(self.__url):
            return True
        return False

    def __loadURL(self, url):
        if not self.__valida_url():
            raise ValueError("URL vazia")
        else:
            self.__url = self.__url.strip()

    def __loadValues(self):
        url_aux = self.__url.strip()

        for i in url_aux.split("?")[1].split("&"):
            prefixo = i.split("=")[0]
            try:
                sufixo = i.split("=")[1]
            except IndexError:
                print("URL invalida: sem parâmetros encontrados")
            else:
                if prefixo.isnumeric():
                    prefixo = float(prefixo)
                if sufixo.isnumeric():
                    sufixo = float(sufixo)

                self.__map[prefixo] = sufixo

    @property
    def url(self):
        return self.__url

    @property
    def base(self):
        chaves = []
        for key in self.__map.keys():
            chaves.append(key)
        return chaves

    @property
    def parametros(self):
        params = []
        for key in self.__map.values():
            params.append(key)
        return params

    def get_valor(self, key):
        return self.__map[key]
