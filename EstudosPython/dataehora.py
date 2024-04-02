from arquivos_recepcao.utilidades import numeros, cores
from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d/%m/%y %Hh% Mmin')
numeros.lin()
print(hora.center(45))
numeros.lin()
cont = 1
soma = 0
for cont in range(1, 5):
    valor = numeros.leiaDinheiro(f'Digite {cont}º valor: ')
    cont += 1
    soma +=valor
cores.verde(f'A soma total dos valores é R$ {soma:.2f}')
numeros.lin()
