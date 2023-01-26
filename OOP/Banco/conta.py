class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def __str__(self):
        return f"{self.__numero} - {self.__titular} - {self.__saldo} - {self.__limite}"

    @property
    def numero(self): return self.__numero

    @property
    def titular(self): return self.__titular

    @property
    def saldo(self): return self.__saldo

    @property
    def limite(self): return self.__limite

    @staticmethod
    def codigo_banco(): return "001"

    def depositar(self, valor): self.__saldo += valor

    def sacar(self, valor): self.__saldo -= valor

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)

