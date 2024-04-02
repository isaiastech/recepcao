from utilitarios.linhas import linhas
from utilitarios import mesnsagems_str
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

print('-'*40)
print('NUMEROS POR EXTENSO V 1.0'.center(40))
print('-'*40)
while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    if 0 < valor <= 20:
        print(f'Você digitou {numeros[valor]}.')
    elif valor > 20:
        print('Valor inválido, digite um valor entre 0 e 20')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if resposta == 'N':
        break
mesnsagems_str.fimdoprograma('')
