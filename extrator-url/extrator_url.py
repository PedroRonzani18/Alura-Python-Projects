class ExtratorURL:
    def __init__(self, url):
        self.__url = url
        self.__map = {}
        self.__loadValues()

    @property
    def url(self): return self.__url

    def getValor(self, key): return self.__map[key]

    def __loadValues(self):
        url_aux = self.__url

        if url_aux.strip() == "":
            print("URL invalida: URL vazia")

        else:
            parametros = url_aux[url_aux.find("?") + 1:]
            encontrados = parametros.split("&")

            for i in encontrados:
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