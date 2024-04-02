import calendar
from datetime import date
mes = int(input('Digite o número do mes: '))
if mes >= 1 and mes <= 12 :
    cal = calendar.month(2020, mes)
    print(f'Esse é o caleandário do mês , {mes}')
    print('')
    print(f'{cal}')
    print('-'*45)
else:
    print('Entrada inválida!!')
hj = date.today()
dias = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo')
print(f'Hoje é , {dias[hj.weekday()]}')
