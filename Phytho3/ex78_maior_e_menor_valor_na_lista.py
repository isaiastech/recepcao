valor = []
maior = 0
menor = 0
for cont in range(0, 5):
    contador = int(input(f'Digite um valor para posição {cont}: '))
    valor.append(contador)
    if cont == 0:
        maior = menor = valor[cont]
    else:
        if valor[cont] > maior:
            maior = valor[cont]
        if valor[cont] < menor:
            menor = valor[cont]
print('=-'*30)
print(f'Você digitou os valores {valor}.')
print(f'O maior valor digitado foi {maior} nas posições .', end=' ')
for i, v in enumerate(valor):
    if v == maior:
        print(f'...{i}')
print(f'O menor valor digitado foi {menor} nas posição', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'...{i}')

