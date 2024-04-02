from utilitarios.linhas import linhas
linhas('')
print('CADASTRE UMA PESSOA '.center(30))
linhas('')
total18 = toH = toM20 = 0
while True:
    idade = int(input('Idade:'))
    Sexo = ' '
    while Sexo not in 'MF':
        Sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >=18:
        total18 +=1
    if Sexo == 'M':
        toH += 1
    if Sexo == 'F' and idade < 20:
        toM20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta= str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos é {total18}')
print(f'Ao todo foram {toH} homems cadastrados.')
print(f'E temos {toM20} mulheres com menos de 20 anos.')
