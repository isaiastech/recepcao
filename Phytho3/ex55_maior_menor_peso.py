maior = 0
menor = 0
for cont in range(1, 6):
    peso = float(input(f'Digite o peso da {cont}º pessoa: '))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg ')
print(f'O menor peso lido foi {menor}Kg')
