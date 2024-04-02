#028 - Jogo da Adivinhação v.1.0
from utilitarios import cores
from time import sleep
from random import randint
print('-=-'*20)
cores.azul('Vou pensar em um número 0 à 5 tente adivinhar...')
print('-=-'*20)
n = int(input('Em que número eu pensei? '))
cores.amarelo('PROCESSANDO...')
sleep(2)
n2 = randint(0, 5)
if n2 == n:
    cores.verde('PARABÉNS! Você conseguiu vencer!')
else:
    cores.vermelho(f'Você Perdeu eu pensei em {n2}')
