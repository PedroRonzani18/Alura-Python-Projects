from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        match len(documento):
            case 11: return DocCpf(documento)
            case 14: return DocCnpj(documento)
            case _: raise ValueError("Quantidade invalida de digitos")


class DocCpf:
    def __init__(self, documento):
        if self.__valida(documento):
            self.__cpf = documento
        else:
            raise ValueError("CPF invalido")

    def __str__(self):
        return self.__format()

    def __valida(self, documento):
            return CPF().validate(documento)

    def __format(self):
        return CPF().mask(self.__cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.__valida(documento):
            self.__cnpj = documento
        else:
            raise ValueError("CNPJ invalido")

    def __str__(self):
        return self.__format()

    def __valida(self, documento):
            return CNPJ().validate(documento)

    def __format(self):
        return CPF().CNPJ(self.__cpf)
