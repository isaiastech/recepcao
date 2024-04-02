#m1 = float(input('Digite a primeira nota: '))
#m2 = float(input('Digite a segunda nota: '))
#soma = (m1 + m2) /2
#print(f'A média entre {m1} e {m2} é igual {soma:.2f}')
c = 1
soma = 0
for c in range(1,4):
    m1 = float(input(f'{c}ª nota: '))
    soma +=m1
print(f'A média das {c} notas é {soma/3:.2f}')
