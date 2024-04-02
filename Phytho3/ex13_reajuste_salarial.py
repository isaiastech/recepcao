sal = float(input('Qual do salário do Funcinário? R$ '))
aumento = (sal * 15/100)
total = (sal + aumento)
print(f'Um funcionário que ganhava R$ {sal}\nCom 15% de aumento passa a receber R${total:.2f}')
