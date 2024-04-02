
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" NÃO É VALIDO!!\033[m')
        else:
            valido = True
            return float(entrada)
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
def lin():
    print('~'*62)

from datetime import timedelta, date
umDia = date.today() + timedelta(days=1)
doisDias = date.today() + timedelta(days=2)

valorCobrado = leiaDinheiro('Valor cobrado: ')
valorComDesconto = leiaDinheiro('Valor com 30% de desconto: ')
varloId = leiaInt('Digite o valor de ID? ')
diferenca = (valorCobrado - valorComDesconto)

umaDiaria = (diferenca * 0.4)
duasDiaria = diferenca * 0.7
tresDiaria = diferenca * 0.9

lin()
print(f'A Comissão uma diária é R$ {umaDiaria:.2f}')
print(f'A Comissão duas diária é R$ {duasDiaria:.2f}')
print(f'A Comissão três diária é R$ {tresDiaria:.2f}')

lin()

print(f"UPDATE comissao_recepcao SET comissao = {duasDiaria:.2f}, numero_de_diarias = '2', saida = '{umDia}' WHERE "
      f"id = '{varloId}';")
print('')
print(f"UPDATE comissao_recepcao SET comissao = {tresDiaria:.2f}, numero_de_diarias = '3', saida = '{doisDias}' "
      f"WHERE id = '{varloId}';")

