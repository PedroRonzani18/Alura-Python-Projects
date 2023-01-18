from datetime import datetime


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        self._idade = self.__age()
        self._salario = salario

    def __str__(self):
        return f"Funcionario: {self._nome}, R${self._salario}, {self.idade}"

    def __age(self):
        bd = self._data_nascimento
        today = datetime.today()
        return today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))

    @property
    def nome(self): return self._nome

    @property
    def sobrenome(self): return self._nome.strip().split(' ')[-1]

    @property
    def data_nascimento(self): return self._data_nascimento

    @property
    def formated_data_nascimento(self): return self.data_nascimento.strftime("%d/%m/%Y")

    @property
    def salario(self): return self._salario

    @property
    def idade(self): return self._idade

    def __verifica_diretoria(self):
        return (self._salario >= 100000) and (self.sobrenome in ['Khan', 'Tudor'])

    def calcula_bonus(self):
        valor = self._salario
        if valor > 1000:
            valor = 0
        return valor

    def decrescimo_salario(self):
        if self.__verifica_diretoria():
            self._salario *= 0.9
