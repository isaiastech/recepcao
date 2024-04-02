pessoas = list()

while True:
    cad = str(input('Nome: ')).title()
    pessoas.append(cad)
    resp = str(input('Quer continuar S/N ? '))
    if resp in 'Nn':
        break
for i, v in enumerate(pessoas):
    print(f'{i+1}º cadastro {v}')
