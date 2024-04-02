from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analizando os valores passados...')
    sleep(1.5)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        if cont == 0:
            maior = maior
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informado {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
