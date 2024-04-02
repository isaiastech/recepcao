# coding: iso-8859-1 -*-
print('CALCULADORA ')
print('Ecolha um operador\n( + ) Adicão\n( - ) Subtração\n( * ) Multiplicaçaõ\n( / ) Divisão\n')
print('Para encerrar o programa digite ( Sair )...')
valor = str(input('Qual calculo gostaria de fazer? '))
if(valor == 'Sair' or 'SAIR'):
    print('Encerrando programa....')
valor1 = int(input('Primeiro valor? '))
valor2 = int(input('Segundo valor? '))
if(valor == '+'):
    print(f'O valor {valor1} + {valor2} é igual {valor1 + valor2}')
elif(valor == '-'):
    print(f'O valor {valor1} - {valor2} é igual {valor1 - valor2}')
elif(valor == '*'):
    print(f'O valor {valor1} * {valor2} é igual {valor1 * valor2}')
elif(valor == '/'):
    print(f'O valor {valor1} / {valor2} é igual {valor1 / valor2}')
else:
    print('Encerrando programa....')

