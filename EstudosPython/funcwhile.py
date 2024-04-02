arquivo = open('problema_utf_8.txt', 'a')
cont = 1
soma = 0
while True:
    num = float(input(f' digite {cont}º valor R$: '))
    cont+=1
    soma +=num
    if num == 0:
        break
print(f'A soma dos valores é R${soma:.2f}')
print(f'A soma dos valores é R${soma :.2f}', file=arquivo)
arquivo.close()
