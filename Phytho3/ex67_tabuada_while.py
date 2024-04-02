#Tabuada com While
from time import sleep
try:
    while True:
        n = int(input('\033[1;31mPARAR O PROGRAMA DIGITE 0\033[m\nQuer ver a tabuada de qual valor? '))
        print('-'*30)
        if n == 00:
            break
        print('-'*30)
        for c in range(1, 11):
            sleep(1)
            print(f'{n} x {c} = {n*c}')
        print('-'*30)
except:
    print('\033[1;31mHOUVE UM ERRO DE DIGITAÇÃO !! TENTE NOVAMENTE \033[m')
print('\033[1;95mPROGRAMA ENCERRADO VOLTE SEMPRE OBRIGADO...\033[m')
