#019 - Sorteando um item na lista
aluno = []
import random
n1 = str(input('Digite o primeiro aluno: ')).title()
n2 = str(input('Digite o segundo aluno: ')).title()
n3 = str(input('Digite o terceiro aluno: ')).title()
n4 = str(input('Digite o quarto aluno: ')).title()
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
