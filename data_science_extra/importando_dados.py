import pandas as pd
import requests
from bs4 import BeautifulSoup


def abrindo_dados_diferentes():
    json = open('dados/aluguel.json')
    # print(json.read()) # printa string bagunçada

    df_json = pd.read_json('dados/aluguel.json')
    # print(df_json) # printa com titutlos em ordem alfabetica

    txt = open('dados/aluguel.txt')
    # print(txt.read()) # printa string tabelada nao identada

    df_txt = pd.read_table('dados/aluguel.txt')
    # print(df_txt) # printa com titulos na ordem do arquivo

    df_xlsx = pd.read_excel('dados/aluguel.xlsx', engine='openpyxl')
    # print(df_xlsx)

    df_html = pd.read_html('dados/dados_html_1.html')
    # print(df_html[0])

    """nao funciona"""
    # df_html_2 = pd.read_html('https://unafiscosaude.org.br/site/tabelas-de-precos-dos-planos-ativos-para-comercializacao/')
    # print(df_html_2[0])

    response = requests.get('https://www.federalreserve.gov/releases/h3/current/default.htm')
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.findAll('table')
    html_file = f'<html><body>{table}</body></html>'
    df_html3 = pd.read_html(html_file)
    print(df_html3)

    # Como a função read_html retorna uma lista de DataFrames, basta acessar as tabelas pelos índices da lista.
    # Como temos três tabelas na página usamos os índices 0, 1 ou 2 para acessar os DataFrames que buscamos df[0]


if __name__ == '__main__':
    pd.options.display.width = 320  # pd.set_option('display.width', 320)
    pd.options.display.max_columns = 10  # pd.set_option('display.max_columns',10)
