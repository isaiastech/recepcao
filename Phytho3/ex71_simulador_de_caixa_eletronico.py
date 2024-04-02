from utilitarios.linhas import linhas
from utilitarios.mesnsagems_str import fimdoprograma
linhas('')
print('BANCO CEV'.center(30))
linhas('')
valor = float(input('Que valor você quer sacar? R$ '))
total = valor
cedulas = 100
totalcedulas = 0
try:
    while True:
        if total >= cedulas:
            total -= cedulas
            totalcedulas += 1
        else:
            if totalcedulas > 0:
                print(f'Total de {totalcedulas} cédulas de R${cedulas}')
            if cedulas == 100:
                cedulas = 50
            elif cedulas == 50:
                cedulas = 20
            elif cedulas == 20:
                cedulas = 10
            elif cedulas == 10:
                cedulas = 5
            elif cedulas == 5:
                cedulas = 2
            elif cedulas == 2:
                cedulas = 1
            totalcedulas = 0
            if total == 0:
                break
except:
    print('Não foi possível evetuar a transação!!')
linhas('')
fimdoprograma('')
