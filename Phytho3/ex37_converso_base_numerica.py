#037 - Conversor de Bases Numéricas
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[ 1 ] Converter para BINÁRIO\n'
      '[ 2 ] Converter par OCTAL\n'
      '[ 3 ] Converter para HEXADECIAMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertito para BINÁRIO é igual {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual {hex(num)[2:]}')
else:
    print('OPÇÃO INVÁLIDA TENTE NOVAMENTE')
