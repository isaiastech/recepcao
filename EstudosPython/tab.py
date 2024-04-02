from arquivos_recepcao.utilidades import cores, numeros
from time import sleep
print('-'*40)
print('\033[1;94mPROGRAMA PARA GERAR TABUADA V 1.01\033[m'.center(40))
print('-'*40)
try:
    while True:
        num = numeros.leiaInt('\033[1;32mDigite um número e veja sua tabuada: \033[m')
        print('-' * 40)
        for cont in range(1, 11):
            sleep(0.2)
            cores.verde(f'{cont} X {num} = {cont * num}\033[m'.center(26))
        resp = str(input('Quer continuar [S/N]? '))
        if resp in "Nn":
            break
except:
    cores.vermelho('ERRO DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
print('-'*40)
cores.verde(f'<<<<'"PROGRAMA ENCERRADO VOLTE SEMPRE!!\033[m'\033[1;32m>>>")
