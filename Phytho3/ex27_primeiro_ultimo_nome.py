#027 - Primeiro e último nome de uma pessoa

n = str(input('Digite seu nome completo: ')).title()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}')
