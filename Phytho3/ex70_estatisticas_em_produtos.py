from utilitarios.linhas import linhas
from utilitarios.mesnsagems_str import fimdoprograma
linhas('')
print('LOJA SUPER BARATAO'.center(40))
linhas('')
contador = 0
total = totmil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço:R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total da compra é R${total:.2f}')
print(f'Temos {totmil} produto custando mais de R$1000.00.')
print(f'O produto mais barato foi {barato} e custou R${menor:.2f}')
fimdoprograma('')
