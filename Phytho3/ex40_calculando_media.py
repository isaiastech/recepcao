n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) /2
print(f'Tirando uma nota {n1} e uma nota {n2} tem um média de {média:.2f}.')
if média >= 7:
    print('O aluno está APROVADO')
elif média >= 5 and média < 7:
    print('O aluno está em RECUPERAÇÃO .')
else:
    print('O aluno está REPROVADO.')
