# !/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import date
def dataextenso():
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    mes_ext = {1 : 'janeiro', 2 : 'fevereiro', 3 : 'março', 4 : 'abril', 5 : 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
               9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    aniver = data_em_texto
    dia, mes, ano = aniver.split("/")
    print('%s de %s de %s' % (dia, mes_ext[int(mes)], ano))

dataextenso()