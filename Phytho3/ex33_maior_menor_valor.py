#Maior e menor valores
lista = []
mai = 0
men = 0
for c in range(1, 6):
    lista.append(int(input(f'{c}º Valor : ')))
    max(lista)
    min(lista)
print('-='*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor foi {max(lista)}')
print(f'O menor valor foi {min(lista)}')
print('-='*20)
