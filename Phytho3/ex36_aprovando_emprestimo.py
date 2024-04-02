#036 - Aprovando Empréstimo
casa = float(input('Valor da casa R$: '))
salário = float(input('Salário do comprador R$: '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salário * 30 / 100
print(f'Para pagar um casa  de {casa:.2f} em {anos} anos, \na prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Emprétimo NEGADO!!')
