números = list()
while True:
    num = int(input('Digite um número:'))
    if num not in números:
        números.append(num)
        print('Valor adicionado com suscesso!!')
    else:
        print('Valor duplicado não é possível adicionar!!')
    resposta = str(input('Quer continuar (S/N): '))
    if resposta in 'Nn':
        break
print('-='*30)
números.sort()
print(f'Os valares adicionados foram {números}')
