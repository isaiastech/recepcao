pessoas = {'nome': 'Isaias', 'Sexo':'M', 'Idade': 39}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos.')
#del pessoas['Sexo']
#pessoas ['nome']= 'Pedro'
pessoas['peso']=98.4
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
