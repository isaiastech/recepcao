from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
vitoria = 0
while True:
    valor = int(input('Diga um valor: '))
    computador = randint(0, 19)
    total = valor + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('PAR OU IMPAR? ')).strip().upper()[0]
    print(f'Você jogou {valor} e computador jogou {computador} total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente....')
print(f'GAME OVER! Você venceu {vitoria} vezes.')




