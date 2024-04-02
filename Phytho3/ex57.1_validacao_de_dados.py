sexo = str(input('Informe seu Sexo [M / F]: ')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, Por favor informe seu Sexo: '))
print(f'Sexo {sexo} registrado com sucesso. ')
