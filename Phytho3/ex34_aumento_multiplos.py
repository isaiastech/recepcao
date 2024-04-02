#034 - Aumentos múltiplos
salario = float(input('Qual o salário do funcinário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f'O funcinário que ganhava R${salario:.2f} passa a ganhar R${novo:.2f}')
else:
    novo = salario + (salario * 10 / 100)
    print(f'O funcinário que ganhava R${salario:.2f} passa a ganhar R${novo:.2f}')
