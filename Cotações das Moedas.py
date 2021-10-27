import requests
from tkinter import *

window = Tk()

def pegar_cotacoes():
    '''Função que realiza as cotações'''
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    {"Dólar":>8}: {cotacao_dolar:<8}
    {"Euro":>8}: {cotacao_euro:<8}
    {"BTC":>8}: {cotacao_btc:<8}'''

    texto_cotacao['text'] = texto

window.title('Cotação Atual das Moedas')  
window.geometry('310x200')  # Tamanho da inicialização da janela

texto_info = Label(window, text='CLIQUE NO BOTÃO PARA ATUALIZAR AS COTAÇÕES.')
texto_info.grid(column=0, row=0, padx=10, pady=10)  # Posição do texto
botao = Button(window, text='Buscar cotações USD / EUR / BTC', command=pegar_cotacoes)
botao.grid(column=0, row=2)  # Posição do botão
texto_cotacao = Label(window, text='')
texto_cotacao.grid(column=0, row=5, pady=12, padx=10)  # Posição da informação da cotação

window.mainloop()
