# coding=UTF-8
# coding: iso-8859-1 -*-
def lin():
    print('~'*62)
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mVALOR INVÁLIDO TENTE NOVAMENTE!!\33[m')
        if ok:
            break
    return valor
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" NÃO É VALIDO!!\033[m')
        else:
            valido = True
            return float(entrada)
def contador(*num):
    cont = 0
    cont2 = 1
    while True:
        valor = float(input(f'{cont2}º valor? ').replace(',', '.'))
        cont2 += 1
        if valor == 0:
            break
        cont += valor
    return cont
def lin():
    print('-'*60)

#Progama principal

from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d-%m-%y ')
lin()
print(f'Atualizar sql Diárias {hora}')
print('PARA FECHAR O PROGRAMA DIGITE 000')
lin()
novoValor= []
id_servicos = []
comanda = 0
total = 0
while True:
    numero = leiaDinheiro('\033[1;34mNovo valor do Serviço?  ')
    comanda = leiaInt('Id Serviços: ')
    novoValor.append(numero)
    id_servicos.append(comanda)
    if numero == 0:
        break
print('')

for novoValor, id_servicos in zip(novoValor,id_servicos):
    print(f"UPDATE servicos SET valor ='{novoValor}', data = now() WHERE id_aptos = '{id_servicos}';")

print('')
print('')
lin()

