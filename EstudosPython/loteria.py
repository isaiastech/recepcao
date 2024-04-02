def escreva(msg):
    tam = len(msg)+4
    print(f'{msg}')
    print('˜'*tam)


#PROGRAMA PRINCIPAL
from datetime import datetime
data = datetime.now()
data = data.strftime('%d-%m-%Y %Hh%Mmin')
from random import randint
from time import sleep
escreva(f'   {data}')
lista = list()
jogos = list()
escreva('    JOGOS DA LOTERIA')
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 25)    #NÚMEROS DISPONÍVEIS PARA SORTEIO
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 15:          #QUANTIDADE DE NÚMEROS A SEREM SORTEADOS
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
escreva(f'  SORTEANDO {quant} JOGOS')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

escreva('         < BOA SORTE! >' )
