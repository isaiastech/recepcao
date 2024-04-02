from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('O que gostaria de fazer? ')
opcao = 0
while opcao != 5:
    print("""    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa""")
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é igual à {n1 + n2}.')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual à {n1 * n2}. ')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre os números {n1} e {n2} o maior é {n1}')
        else:
            print(f'Entre os números {n1} e {n2} o maior é {n2}.')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\t\tFINALIZANDO ...')
        sleep(2)
        print('FIM DO PROGAMA VOLTE SEMPRE')
    else:
        print('OPÇÃO INVÁLIDA . TENTE NOVAMENTE...')
    print('=-='*10)
    sleep(2)
