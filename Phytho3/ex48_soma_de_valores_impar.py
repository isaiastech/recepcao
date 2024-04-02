cont = 0
soma = 0
for num in range(1, 10, 2):
    if num % 3 == 0:
        cont += 1
        soma += num
print(f'A soma dos valores {cont} solicitados é {soma}')
