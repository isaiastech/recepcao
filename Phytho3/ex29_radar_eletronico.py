#029 - Radar eletrônico
from utilitarios import cores
velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    cores.vermelho('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    cores.amarelo(f'Você deve pagar o valor de R${multa:.2f}')
cores.verde('Tenha um bom dia! dirija com segurança!')


