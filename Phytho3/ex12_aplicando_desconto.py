preco =float(input('Qual o preço do produto ? '))
desconto = (preco*5)/100
print(f'O produto que custava {preco}, na promoção com desconto de 5% vai custar R${preco-desconto:.2f} ')
