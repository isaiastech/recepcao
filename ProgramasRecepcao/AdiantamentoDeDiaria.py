# coding: iso-8859-1 -*-
apto = str(input('N�mero do apto? '))
dia = int(input('Quantidades de di�rias pagas? '))
fatura = str(input('N�mero da ficha raz�o? '))
gara = int(input('Quantidades de garagem? '))
nota = int(input('N�mero da nota fiscal? '))
if gara >=1 and nota >=1:
    print(f'O apto {apto} pagou {dia} Di�ria e {gara} garagem fatura: {fatura} e a nota fiscal n�mero:{nota}'.upper())
elif gara >=1 and nota <1:
    print(f'O apto {apto} pagou {dia} Di�ria e {gara} garagem fatura: {fatura} e a nota fiscal n�o foi emitida.'.upper())
elif gara <1 and nota <1:
    print(f'O apto {apto} pagou {dia} di�ria com ficha raz�o:{fatura} e a nota fiscal n�o foi emitida.'.upper())
elif gara <1 and nota >1:
    print(f'O apto {apto} pagou {dia} di�ria com ficha raz�o:{fatura} e a nota fiscal n�mero:{nota}'.upper())
