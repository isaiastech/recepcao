# -*- encoding: utf-8 -*-

def contador(*num) :
    cont = 0
    cont2 = 1
    while True:
        valor = float(input(f'{cont2}º valor? ').replace(',', '.'))
        cont2 += 1
        if valor == 0:
            break
        cont += valor
    return cont


#Programa principal
contagem = []
preco  = float(input('valor por Kg R$? ').replace(',', '.'))
contagem.append(contador())
Total = preco * contagem[0]
print(f'O peso total foi Kg {contagem[0]:.2f}')
print(f'O total à pagar é R$ {Total:.2f}')
