from math import factorial
from time import sleep
num = int(input('Digite um número e veja seu fatorial: '))
print('CALCULANDO .....')
sleep(2)
print(f'O fatorial {num}! é {num} x', end=' ')
for cont in range(1, num).__reversed__():
    print(f'{cont}', end=' ')
    print('x'if cont > 1 else '= ', end=' ')
print(factorial(num))
