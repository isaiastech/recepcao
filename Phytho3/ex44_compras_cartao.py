loja = str("LOJAS BATISTA")
linhas= str('='*10)
print(f'{linhas} {loja} {linhas}')
preco = float(input('Preço das compras: R$ '))
print('''Formas de pagamento
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2 x no cartão
[ 4 ] 3 x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    par = total / 2
    print(f'Sua compra será parcelada em 2X de R${par:.2f}')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcela? '))
    parcela = preco / totalparc
    print(f'Sua compra parcelada em {totalparc} X vai custar R${total:.2f} COM JUROS DE 20%')
else:
    total = 0
    print('Opção Inválida Tente novamente!!')
print(f'Sua Compra de R${preco:.2f} vai custar R${total:.2f}')
