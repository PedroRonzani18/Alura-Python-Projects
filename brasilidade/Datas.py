from datetime import datetime, timedelta


class Datas:
    def __init__(self):
        self.__momento_cadastro = datetime.today()

    def __str__(self):
        return self.__format_data()

    def get_momento_cadastro(self):
        return self.__momento_cadastro

    def get_mes_cadastro(self):
        meses = ["janeiro", "fevereiro", "março", "abril", "maior", "junho", "julho", "agosto", "setembro", "outubro",
                 "novembro", "dezembro"]
        return meses[self.__momento_cadastro.month - 1]

    def get_dia_semana_cadastro(self):
        dias = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
        return dias[self.__momento_cadastro.weekday()]

    def __format_data(self):
        return self.__momento_cadastro.strftime("%d/%m/%Y %H:%M")

    def tempo_cadastrado(self):
        return datetime.today() - self.__momento_cadastro
