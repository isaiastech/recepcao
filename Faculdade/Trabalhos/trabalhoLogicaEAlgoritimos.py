
print('--'*30)

print('Bem vindo a Loja do Isaias Batista RU:3993994 v1.0')

print('--'*30)

valorru3993994 = float(input('Entre com o valor do produto: '))
quant= int(input('Entre com o valor da quantidade: '))
if(quant <= 9):
    print(f'Valor sem desconto foi de R$ {valorru3993994 * quant:.2f}')
    #calculo feito dentro do print sem usar uma variável de resposta
elif quant <= 99:
    total = valorru3993994 * quant
    desc3993994 = total - (total * 5 /100)
    print(f'O Valor sem desconto foi R${valorru3993994 * quant:.2f}')
    print(f'O valor com desconto foi R${desc3993994:.2f} com desconto de 5%')
    #Calcula desconto de 5%
elif quant <= 999:
    total1 = valorru3993994 * quant
    desc3993994 = total1 - (total1 * 10 / 100)
    print(f'O Valor sem desconto foi R${valorru3993994 * quant:.2f}')
    print(f'O valor com desconto foi R${desc3993994:.2f} com desconto de 10%')
    #Calcula valor de 10%
else:
    total3993994 = valorru3993994 * quant
    desc3993994 = total3993994 - (total3993994 * 15 / 100)
    print(f'O Valor sem desconto foi R${valorru3993994 * quant:.2f}')
    print(f'O valor com desconto foi R${desc3993994:.2f} com desconto de 15%')
print('Desvenvolvido por Isaias Batista RU:3993994')
