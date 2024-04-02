valort = list()
valores = list()
valoresimpar = list()
while True:
    valor = int(input('Digite um valor: '))
    valort.append(valor)
    if valor % 2 == 0:
        valores.append(valor)
    else:
        valoresimpar.append(valor)
    resposta = str(input('Quer continuar? S/N: '))
    if resposta in 'Nn':
        break
print(f'A lista completa é {valort}')
print(f'Os valores pares foram {valores}')
print(f'Os valores impares foram {valoresimpar}')
