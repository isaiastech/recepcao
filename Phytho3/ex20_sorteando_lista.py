#020 - Sorteando uma ordem na lista
from random import shuffle
n1 = str(input('Primeiro Aluno: ')).title()
n2 = str(input('Segundo Aluno: ')).title()
n3 = str(input('Terceiro Aluno: ')).title()
n4 = str(input('Quarto  Aluno: ')).title()
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)



