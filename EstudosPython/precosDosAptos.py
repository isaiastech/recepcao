# coding: iso-8859-1 -*-
#Arquivo criado em 30/07/2020
def linhas(msg):
    print('-'*58)


aptosEx = ["Single", 252.00, "Duplo ou casal", 310.00, "Conj.Triplo",
         450.00, "Conj.Quadruplo", 555.00, 'Cama Extra', 90.00, 'Garagem', 18.00]
aptosSup = ["Single", 310.00, "Duplo ou casal", 398.00, "Conj.Triplo",
          535.00, "Conj.Quadruplo", 635.00, "Suíte single", 410.00, "Suíte Casal", 450.00]
tip = str('EXECUTIVO')
tips = str('SUPERIOR')
bal = str('Balcão')
des10 = str('10%')
des20 = str('20%')
des30 = str('30%')
linhas('')
print(f'{tip:>8}{bal:>14}{des10:>8}{des20:>12}{des30:>12}')
linhas('')
print(f'{aptosEx[0]:.<15}R${aptosEx[1]:.>5.2f}...R${aptosEx[1]-aptosEx[1]* 10 / 100:.2f}...'
      f'R${aptosEx[1]-aptosEx[1]* 20 / 100:.2f}...R${aptosEx[1]-aptosEx[1]* 30 / 100:.2f}')
#Duplo Casal pos 2 preço pos 3
print(f'{aptosEx[2]:.<15}R${aptosEx[3]:.>5.2f}...R${aptosEx[3]-aptosEx[3]* 10 / 100:.2f}...'
      f'R${aptosEx[3]-aptosEx[3]* 20 / 100:.2f}...R${aptosEx[3]-aptosEx[3]* 30 / 100:.2f}')
#Triplo pos 4 preco 5
print(f'{aptosEx[4]:.<15}R${aptosEx[5]:.>5.2f}...R${aptosEx[5]-aptosEx[5]* 10 / 100:.2f}...'
      f'R${aptosEx[5]-aptosEx[5]* 20 / 100:.2f}...R${aptosEx[5]-aptosEx[5]* 30/ 100:.2f}')
#Quadruplo pos 6 preço pos 7
print(f'{aptosEx[6]:.<15}R${aptosEx[7]:.>5.2f}...R${aptosEx[7]-aptosEx[7]* 10 / 100:.2f}...'
      f'R${aptosEx[7]-aptosEx[7]* 20 / 100:.2f}...R${aptosEx[7]-aptosEx[7]* 30 / 100:.2f}')
linhas('')
print(f'{tips:>8}{bal:>14}{des10:>8}{des20:>12}{des30:>12}')
linhas('')
print(f'{aptosSup[0]:.<15}R${aptosSup[1]:.>5.2f}...R${aptosSup[1]-aptosSup[1]* 10 / 100:.2f}...'
      f'R${aptosSup[1]-aptosSup[1]* 20 / 100:.2f}...R${aptosSup[1]-aptosSup[1]* 30 / 100:.2f}')
#Duplo Casal pos 2 preço pos 3
print(f'{aptosSup[2]:.<15}R${aptosSup[3]:.>5.2f}...R${aptosSup[3]-aptosSup[3]* 10 / 100:.2f}...'
      f'R${aptosSup[3]-aptosSup[3]* 20 / 100:.2f}...R${aptosSup[3]-aptosSup[3]* 30 / 100:.2f}')
#Triplo pos 4 preco 5
print(f'{aptosSup[4]:.<15}R${aptosSup[5]:.>5.2f}...R${aptosSup[5]-aptosSup[5]* 10 / 100:.2f}...'
      f'R${aptosSup[5]-aptosSup[5]* 20 / 100:.2f}...R${aptosSup[5]-aptosSup[5]* 30/ 100:.2f}')
#Quadruplo pos 6 preço pos 7
print(f'{aptosSup[6]:.<15}R${aptosSup[7]:.>5.2f}...R${aptosSup[7]-aptosSup[7]* 10 / 100:.2f}...'
      f'R${aptosSup[7]-aptosSup[7]* 20 / 100:.2f}...R${aptosSup[7]-aptosSup[7]* 30 / 100:.2f}')
#Suíte Casal pos 8 preço 9
print(f'{aptosSup[8]:.<15}R${aptosSup[9]:.>5.2f}...R${aptosSup[9]-aptosSup[9]* 10 / 100:.2f}...'
      f'R${aptosSup[9]-aptosSup[9]* 20 / 100:.2f}...R${aptosSup[9]-aptosSup[9]* 30 / 100:.2f}')
#Suíte Casal pos 10 preço 11
print(f'{aptosSup[10]:.<15}R${aptosSup[11]:.>5.2f}...R${aptosSup[11]-aptosSup[11]* 10 / 100:.2f}...'
      f'R${aptosSup[11]-aptosSup[11]* 20 / 100:.2f}...R${aptosSup[11]-aptosSup[11]* 30 / 100:.2f}')
print(f'{aptosEx[8]:.<15}R${aptosEx[9]:.>5.2f}....{aptosEx[10]:}....R${aptosEx[11]:.2f}')
linhas('')
