temp = []
prin = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(prin) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar S/N? '))
    if resp in 'nN':
        break
print('-='*30)
print(f'Ao todo foram cadastrados {len(prin)} pessoas.')
print(f'O maior peso foi {mai}kg. Peso de ', end='')
for p in prin:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {men}Kg')
