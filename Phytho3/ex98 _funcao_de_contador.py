from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print('-='*20)
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont +=p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')



#Programa principal
contador(1, 10, 1)
contador(10, 1, 1)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
