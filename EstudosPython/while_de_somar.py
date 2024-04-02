soma = 0
cont = 1
while True:
    nome = int(input(f'{cont}º Valor: '))
    cont +=1
    soma += nome
    if nome == 0:
        break
print(f'Você digitou {cont-2} valores.')
print(f'A soma total foi {soma} .')
