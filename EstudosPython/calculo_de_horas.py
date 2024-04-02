import arquivos_recepcao.utilidades
salario = float(input('Valor do Salário base? R$ '))
horasextra = float(input('Quantidade de horas extras 50%? '))
horasextra100 = float(input('Quantidade de horas 100 %? '))
horasmes = (salario / 220)
horas50 = (horasmes * 50 / 100) + horasmes
horas100 = (horasmes * 100 /100) + horasmes
totextra50 = (horasextra * horas50)
totextra100 = (horasextra100 * horas100)
soma = totextra50 + totextra100
arquivo_STR.linhas()
print(f'Valor da hora trabalhada R${horasmes:.2f}')
print(f'Horas extra R${horas50:.2f}')
print(f'Horas extras R${horasextra100:.2f}')
arquivo_STR.linhas()
print(f'O total de horas 50% é R${totextra50:.2f}')
print(f'O total de horas extras 100% é R${totextra100:.2f}')
arquivo_STR.linhas()
print(f'A soma total das horas é R${soma:.2f}')
