from random import randint
comp = randint(0, 10)
print("""Sou seu computador e acabei de pensar um número entre 0 à 10...
Será que você consegue adivinhar...""")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('Mais tente novamente!!!')
        elif jogador > comp:
            print('Menos...tente novamente!!!')
print(f'Acertou com {palpite} Tentativas PARABÉNS')
