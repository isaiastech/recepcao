# coding: iso-8859-1 -*-
from arquivos_recepcao.utilidades import cores
cont = 0
soma = 0
for cont in range(0, 6):
    caixa_cart = int(input(f'{cont+1}� caixa de Cart�o: '))
    soma += caixa_cart
cart_casa = int(input('Total de Cart�o com hospedes? '))
totalcart = (soma + cart_casa)
if totalcart == 300:
    cores.verde('Os cart�es est�o corretos n�o falta nada!!')
elif totalcart < 300:
    cores.vermelho(f'Est� faltando {300 - totalcart} cart�es!!')
else:
    cores.azul(f'Est� sobrando {totalcart - 300} cart�es.')
