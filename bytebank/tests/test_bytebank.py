from src.bytebank import Funcionario
from pytest import mark


class TestClass:
    def test_quando_recebe_18_04_2004_idade_deve_retornar_18(self):
        entrada = "18/04/2004"
        espero = 18

        funcionario_teste = Funcionario("pedro", entrada, 2000)

        resultado = funcionario_teste.idade

        assert resultado == espero

    def test_calculando_desconto(self):
        entrada = 100000
        espera = 90000

        funcionario_teste = Funcionario("Pedro Khan", "18/04/2004", entrada)
        funcionario_teste.decrescimo_salario()

        resultado = funcionario_teste.salario

        assert resultado == espera

    @mark.calcular_bonus
    def test_calcula_bonus(self):
        entrada = 10000
        espera = 0
        funcionario = Funcionario("Pedro Khan", "10/04/2004", entrada)

        resultado = funcionario.calcula_bonus()

        assert resultado == espera
