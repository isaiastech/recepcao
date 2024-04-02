galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro sexo inválido!!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apena S ou N')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo foram cadastrado {len(galera)} pessoas.')
média = soma / len(galera)
print(f'B) A média de idade é {média:.2f} anos.')
print(f'C) Os homens cadastrados foram: ', end=' ')
for p in galera:
    if p['sexo'] in 'Mm':
        print(f'{p["nome"]}', end=' ')
print()
print(f'D) A mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('E) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('       ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('')
print('<< ENCERRADO>>')
