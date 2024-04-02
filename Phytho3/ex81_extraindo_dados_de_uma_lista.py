lista = []
while True:
    n = int(input('Digite um número: '))

    lista.append(n)
    resposta = str(input('Quer continuar [S/N]: '))
    if resposta in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista} ')
if 5 in lista:
    print('O numero 5 está na lista')
else:
    print('O número 5 não está na lista.')
