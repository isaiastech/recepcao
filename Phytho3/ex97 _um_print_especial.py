def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'{msg}'.center(tam))
    print('~'*tam)


escreva('ola mundo')
escreva('OI')
escreva('Isaias Batista')
