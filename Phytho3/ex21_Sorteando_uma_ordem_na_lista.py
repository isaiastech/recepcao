from random import shuffle
lista = []
cont = 0
for cont in range(1, 6):
    aluno = str(input(f'{cont} Aluno : ')).title()
    aluno = lista.append(aluno)
shuffle(lista)
print(f'A ordem de apresentação será: {lista}')
