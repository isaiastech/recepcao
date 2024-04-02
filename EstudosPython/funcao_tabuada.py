# coding: iso-8859-1 -*-
from time import sleep
def tabuada(x) ->int:
    for c in range(1, 11):
        sleep(0.5)
        print(f'{c:>2} x {x} = {c*x:>2} ')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mVALOR INVÁLIDO TENTE NOVAMENTE!!\33[m')
        if ok:
            break
    return valor



n = leiaInt('Qual tabuada? ')
tabuada(n)
