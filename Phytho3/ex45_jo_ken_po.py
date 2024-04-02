from random import randint
from time import sleep
from utilitarios import cores
try:
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    cores.verde('Escolha suas opções:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura \033[m')
    jogador = int(input('Qual é sua escolha? '))
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(1)
    print('-=' * 15)
    print(f'Computador jogou {itens[computador]}'.center(30))
    print(f'O jogador jogou {itens[jogador]}'.center(30))
    print('-=' * 15)
    if computador == 0 and jogador == 0:
        cores.amarelo('Jogo EMPATADO')
    elif computador == 1 and jogador == 1:
        cores.amarelo('Jogo empatado')
    elif computador == 2 and jogador == 2:
        cores.amarelo('Jogo Empatado')
    elif computador == 1 and jogador == 0:
        cores.verde('Computador Ganhou!!')
    elif computador == 2 and jogador == 1:
        cores.verde('Computador Ganhou !!')
    elif computador == 0 and jogador == 2:
        cores.verde('Computador Ganhou!!')
    elif jogador == 0 and computador == 2:
        cores.azul('O jogador Ganhou !!!')
    elif jogador == 1 and computador == 0:
        cores.azul('O jogador Ganhou!!!')
    elif jogador == 2 and computador == 1:
        cores.azul('O jogador Ganhou !!')
    else:
        cores.vermelho('Opção INVÁLIDA')
except:
    cores.vermelho('VOCÊ ESCOLHEU UM VALOR INVÁLIDO !! TENTE NOVAMENTE....')
