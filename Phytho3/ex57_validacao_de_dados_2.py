while True:
    sexo = str(input('Informe seu Sexo [ M/F ]: ')).strip().upper()
    if sexo == 'M':
        print(f'Sexo {sexo} registrado com suscesso!!')
        break
    elif sexo == 'F':
        print(f'Sexo {sexo} registrado com suscesso!!')
        break
    else:
        print('SEXO INVÁLIDO: ')

