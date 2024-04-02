#039 - Alistamento Militar
from datetime import date
ano = date.today().year
idade = int(input('Ano de nascimento: '))
atual = date.today().year
nascimento = (atual - idade)
print(f'Quem nasceu em {idade} tem {nascimento} anos em {ano}')
if nascimento == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif nascimento < 18:
    saldo = 18 - nascimento
    print(f'Ainda faltam {saldo} para seu alistamento.')
    ano2 = atual + saldo
    print(f'Seu alistamento será em {ano2}.')
elif nascimento > 18:
    saldo = nascimento - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano3 = atual - saldo
    print(f'Seu alistamento foi em {ano3}.')
