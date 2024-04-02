from time import sleep
from random import randint
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6), 'Jogador2':randint(1, 6),
        'Jogador3': randint(1, 6), 'Jogador4':randint(1, 6)}
ranking = list()
print('-'*30)
print('Valores Sorteados'.center(30))
print('-'*30)
for k, v in jogo.items():
    sleep(1)
    print(f'{k} tirou {v} no dado')
print('-'*30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'<<<<<<< Ranking  >>>>>>>>'.center(30))
print('-'*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

