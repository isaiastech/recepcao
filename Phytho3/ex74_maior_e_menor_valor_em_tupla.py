from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}  ', end='')
print(f'\nO maior valor é {max(numeros)}.')
print(f'O nemor valor é {min(numeros)}.')
