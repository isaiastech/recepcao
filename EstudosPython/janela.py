# -*- encoding: utf-8 -*-
import PySimpleGUI as sg


class TelaPython:
    def _init_(self):
        # layout
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button('Enviar Dados')]
        ]
        # Janela
        janela = sg.Window('Dados do Usuário').layout(layout)
        # Extrair dados da tela
        self.button, self.values = janela.read()

    def iniciar(self):
        print(self.values)

TelaPython()
