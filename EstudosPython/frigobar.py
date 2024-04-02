# coding: iso-8859-1 -*-
def lin(ms):
    return print('-'*50)


frigobar =['01-Água de coco',703 ,'02-Água com Gas', 705, '04-Água sem Gas',710 ,
           '02-Batata', 725, '01-Castanha de Caju',730,
           '02-Cerveja Brahma',743 , '02-Cerveja Heineken',912 ,
           '02-Lacta 5 Star',757 ,  '02-Diamante Negro',755 ,
           '02-Unidades-Prestigio', 760, '01-Nescau',770 , '03-Coca_cola',775 ,
           '02-Guaraná',780 , '02-Copo de vidro',793]
consumo = []
lin('')
print('PRODUTOS DO FRIGOBAR'.center(50))
lin('')
for pos in range(0, len(frigobar)):
    if pos % 2 == 0:
        print(f'{frigobar[pos]:.<33}', end='')
    else:
        print(f'{frigobar[pos]:.>6}')
lin('')
while True:
    produtos = int(input('Consumo cod.: '))
    quat = int(input('Quantidade? '))
    if quat == 0:
        break
    elif produtos == 703:
        consumo.append(quat)
        consumo.append('Água de coco')
    elif produtos == 755:
        consumo.append(quat)
        consumo.append('Diamante negro')
    elif produtos == 705:
        consumo.append(quat)
        consumo.append('Água com Gas')
    elif produtos == 710:
        consumo.append(quat)
        consumo.append('Água sem gas')
    elif produtos == 725:
        consumo.append(quat)
        consumo.append('Batata')
    elif produtos == 730:
        consumo.append(quat)
        consumo.append('Castanha de Caju')
    elif produtos == 743:
        consumo.append(quat)
        consumo.append('Cerveja Brahma')
    elif produtos == 912:
        consumo.append(quat)
        consumo.append('Cerveja Heineken')
    elif produtos == 757:
        consumo.append(quat)
        consumo.append('Lacta 5 Star')
    elif produtos == 760:
        consumo.append(quat)
        consumo.append('Unidades-Prestigio')
    elif produtos == 770:
        consumo.append(quat)
        consumo.append('Nescau')
    elif produtos == 775:
        consumo.append(quat)
        consumo.append('Coca_cola')
    elif produtos == 780:
        consumo.append(quat)
        consumo.append('Guaraná')
    elif produtos == 793:
        consumo.append(quat)
        consumo.append('Copo de vidro')
lin('')
print('CONSUMO DO FRIGOBAR'.center(30))
lin('')
print('Quant.')
for pos in range(0, len(consumo)):
    if pos % 2 == 0:
        print(f'{consumo[pos]:.<6}', end='')
    else:
        print(f'{consumo[pos]:.>6}')
