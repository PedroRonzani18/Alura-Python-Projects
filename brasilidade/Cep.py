import requests

class Cep:
    def __init__(self, cep):
        if self.__valida_cep(str(cep)):
            self.__cep = str(cep)
        else:
            raise ValueError("CEP invalido")

    def __valida_cep(self, cep):
        return len(cep) == 8

    def dados_cep(self):
        return requests.get(f"https://viacep.com.br/ws/{self.__cep}/json/").json()
