class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self): return self.__numero

    @numero.setter
    def numero(self, numero): self.__numero = numero

    def getTitular(self): return self.__titular
    def getSaldo(self): return self.__saldo
    def getLimite(self): return self.__limite

    def depositar(self, valor): self.__saldo += valor

    def sacar(self, valor): self.__saldo -= valor

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
