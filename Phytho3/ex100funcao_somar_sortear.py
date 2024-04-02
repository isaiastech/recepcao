from random import randint
from time import sleep

def sortea(lista):
    print('Sorteando 5 Valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares de {lista}, temos {soma}.')



#Programa principal
números = list()
sortea(números)
somapar(números)
