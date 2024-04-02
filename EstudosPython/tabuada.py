from arquivos_recepcao.utilidades import cores
from time import sleep

while True:
    tab = int(input('\033[1;31mDigite um número e veja a tabuada? '))
    for cont in range(1, 11):
        sleep(0.3)
        cores.azul(f'{cont} x {tab} = {cont * tab}')
    res = str(input('Quer continuar ( S/N ) ? ')).upper()[0]
    if res == 'N':
        break
cores.verde('Obrigado volte Sempre')
