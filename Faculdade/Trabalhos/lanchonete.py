print('*'*53)
print('Bem vindo a Lanchonete do Isaias Batista Ru:3993994')#Menu Cardápio
print('*************** Cardápio *******************')
print('| Código |       Descrição           | Valor |')
print('| 100    | Cachorro-Quente           | 9,00  |')
print('| 101    | Cachorro-Quente Duplo     | 11,00 |')
print('| 102    |       X-Egg               | 12,00 |')
print('| 103    |       X-Salada            | 13,00 |')
print('| 104    |       X-Bacon             | 14,00 |')
print('| 105    |       X-Tudo              | 17,00 |')
print('| 200    | Refrigerante Lata         | 5,00  |')
print('| 201    |     Chá Gelado            | 4,00  |')
ru3993994 = [9, 11, 12, 13, 14, 17, 5, 4] #Lista com valores dos produtos
cont = 0    # contador do while
total = 0   #soma os valores do while
while True:
    produtoRu3993994 = int(input('Entre com o código desejado: '))
    while(produtoRu3993994 != 100) and (produtoRu3993994 != 101) and (produtoRu3993994 != 102)and \
            (produtoRu3993994 != 103) and (produtoRu3993994 != 104) and (produtoRu3993994 !=105)and \
            (produtoRu3993994 != 200) and (produtoRu3993994 != 201):
        print('Opção Inválida!!')
        produtoRu3993994 = int(input('Entre com o código desejado: '))

    if produtoRu3993994 == 100:  #Satisfazer a primeira condição
        cont += 1
        total += ru3993994[0] #Calcular o produto com base no valor da lista
        print(f'Você pediu um Cachorro-Quente no valor de R${ru3993994[0]:.2f}') #retorna o valor da lista
        pedido = int(input('Deseja pedir mais alguma coisa? \n1 - sim\n0 - Não\n>>> '))
        if pedido == 2:
            break
    elif produtoRu3993994 == 101:
            cont += 1
            total += ru3993994[1]
            print(f'Você pediu um Cachorro-Quente Duplo no valor de R${ru3993994[1]:.2f}')#retorna o valor da lista
            pedido = int(input('Deseja pedir mais alguma coisa? \n1 - sim\n0 - Não\n>>> '))
            if pedido == 0:
                break
    elif produtoRu3993994 == 102:
            cont += 1
            total += ru3993994[2]
            print(f'Você pediu um  X-Egg no valor de R${ru3993994[2]:.2f}')  # retorna o valor da lista
            pedido = int(input('Deseja pedir mais alguma coisa? \n1 - sim\n0 - Não\n>>> '))
            if pedido == 0:
             break
    elif produtoRu3993994 == 103:
            cont += 1
            total += ru3993994[3]
            print(f'Você pediu um  X-Salada no valor de R${ru3993994[3]:.2f}')
            pedido = int(input('Deseja pedir mais alguma coisa? \n1 - sim\n0 - Não\n>>> '))
            if pedido == 0:
             break
    elif produtoRu3993994 == 104 :
            cont += 1
            total += ru3993994[4]
            print(f'Você pediu um  X-Bacon no valor de R${ru3993994[4]:.2f}')
            pedido = int(input('Deseja pedir mais alguma coisa? \n1 - sim\n0 - Não\n>>> '))
            if pedido == 0:
             break
    elif produtoRu3993994 == 105:
            cont += 1
            total += ru3993994[5]
            print(f'Você pediu um  X-Tudo no valor de R${ru3993994[5]:.2f}')
            pedido = int(input('Deseja pedir mais alguma coisa? \n1 - sim\n0 - Não\n>>> '))
            if pedido == 0:
                break
    elif produtoRu3993994 == 200:
            cont += 1
            total += ru3993994[6]
            print(f'Você pediu um  Refrigerante Lata no valor de R${ru3993994[6]:.2f}')
            pedido = int(input('Deseja pedir mais alguma coisa? \n1 - sim\n0 - Não\n>>> '))
            if pedido == 0:
                break
    elif produtoRu3993994 == 201:
            cont += 1
            total += ru3993994[7]
            print(f'Você pediu um  Chá Gelado no valor de R${ru3993994[7]:.2f}')
            pedido = int(input('Deseja pedir mais alguma coisa? \n1 - sim\n0 - Não\n>>> '))
            if pedido == 0:
                break

print(f'O valor a ser pago é : R$ {total:.2f}')
print('Desvenvolvido por Isaias Batista RU:3993994')
