from arquivos_recepcao.utilidades import numeros, cores
from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d-%m-%Y às %H:%M')
print(hora)
cont = 1
soma =0
numeros.lin()
try:
    while True:
        num = numeros.leiaDinheiro(f'Digite o {cont}º Valor: ')
        cont += 1
        soma +=num
        if num == 0:
            break
except:
    print('\033[1;31mERRO VALOR DIGITADO ERRADO!!\033[m')
cores.vermelho(f'A soma dos valores digitados foi R${soma:.2f}')
numeros.lin()
