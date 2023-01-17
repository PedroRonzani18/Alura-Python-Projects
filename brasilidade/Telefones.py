import re


class Telefones:
    def __init__(self, telefone):
        if self.__valida_telefone(telefone):
            self.__numero = telefone
        else:
            raise ValueError("Numero incorreto")

    def __str__(self):
        return self.format_numero()

    def __valida_telefone(self, telefone):
        if re.findall("([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})", telefone):
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.__numero)
        return f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"