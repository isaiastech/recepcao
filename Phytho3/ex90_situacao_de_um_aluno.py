aluno = dict()
while True:
    aluno['Nome'] = str(input('Nome: ')).title()
    aluno['Média'] = float(input('Média: '))
    resp = str(input('Quer continuar? S/N > '))
    if resp in 'Nn':
        break
    if aluno['Média'] >= 7:
        aluno['Situação'] = 'Aprovado'
    elif 5 <= aluno['Média'] < 7:
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'
    for k, v in aluno.items():
        print(f'{k} é igual a {v}')
