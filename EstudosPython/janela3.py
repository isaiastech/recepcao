import PySimpleGUI as sg

#definir janela
layout = [[sg.Text("Qual é seu nome? ")],
         [sg.Input()],
          [sg.Text('Qual sua idade?')],
          [sg.Input()],
            [sg.Button("OK")],]
#Criar a janela
window = sg.Window("Minha Janela", layout)
#interface da janela
event, values = window.read()
#escreve no console
print('Olá', values[0], "! Obrigado por usar o sistema")
print('você tem ', values[1], 'anos.')
window.close()
