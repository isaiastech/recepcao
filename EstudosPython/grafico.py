# coding: iso-8859-1 -*-
import PySimpleGUI as sg
from PySimpleGUI import Window

sg.theme('DarkAmber')
class TelaPython :
    def __init__(self) :
        # Layout
        layout = [
            [sg.Text('Nome'), sg.Input(size=(20, 0), key='nome')],
            [sg.Text('Idade'), sg.Input(size=(20, 0), key='idade')],
            [sg.Text('Profissão'), sg.Input(size=(20,0), key='Profissão')],
            [sg.Text('Qual provedor de e-mail são aceitos:')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'),
             sg.Checkbox('Yahooo', key='yahoo')],
            [sg.Button('Enviar Dados')]
        ]
        # Janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        self.button, self.values = janela.read()
        # Extrair Dados da Janela

    def iniciar(self):
        nome = self.values['nome']
        idade = self.values['idade']
        Profissão = self.values['Profissão']
        aceita_gmail = self.values['gmail']
        aceita_outlook = self.values['outlook']
        aceita_yahoo = self.values['yahoo']
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')
        print(f'Profissão: {Profissão}')
        print(f'aceita Gmail: {aceita_gmail}')
        print(f'aceita outlook: {aceita_outlook}')
        print(f'aceita Yahoo: {aceita_yahoo}')


tela = TelaPython()
tela.iniciar()
