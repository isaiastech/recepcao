numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    if 0 < valor <= 20:
        break
print(f'Você digitou {numeros[valor]}.')

