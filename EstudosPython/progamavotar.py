from datetime import datetime
dataatual = datetime.today().year
print('-='*15)
print('PROGRAMA PARA VOTAR'.center(30))
print('-='*15)
nome = str(input('Digite seu nome: '))
idade = int(input('Ano de nascimento: '))
ano = dataatual - idade
if ano < 16:
    print('Você não pode votar.')
else:
    print('Você ja pode votar.')
print(f'{nome} tem {ano} anos.')
