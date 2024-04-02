print('-'*40)
print('PROGRAMA DE TABUADA V 1.0'.center(40))
print('-'*40)
try:
    num =  int(input('Digite um número e veja sua tabuada: '))
    print('-'*40)
    for i in range (1,11):
        print(f'{i} x {num} = {num*i}'.center(16))
except:
    print('\033[1;31mHouve um erro Você digitou um valor inválido!!\033[m')
print('-'*40)
