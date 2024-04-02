# -*- encoding: utf-8 -*-
#Código acima utilizado porque o pycharm não aceitava acentuação .

def borda(s: str):
#Código copiado da aula de funções do  Prof. Me. Eng. Renan Portela Jorge.
    titulo = len(s)
    if titulo:
        print('+', '-' * titulo,'+')
        print('|', s, '|')
        print('+', '-' * titulo,'+')
#Funções utilizadas no código.
def InteiroRU3993994(msg):
# def para verificar se o valor é numérico.
    ok = False
    valor = 0
    try:
        while True:
            cm = str(input(msg))
            if cm.isnumeric():
                valor = int(cm)
                ok = True
            else:
                print('VOCÊ DIGITOU ALGUMA DIMENSÃO DO OBJETO COM VALOR NÃO NUMÉRICO\nPOR FAVOR ENTRE COM OS VALORES '
                      'NOVAMENTE')
            if ok:
                break
        return valor
    except:
        print('DIGITE UM NÚMERO INTEIRO')

def validapeso(msg):
    #validar o peso
    #Recebe uma mensagem
    valido = False
    while not valido:
        #verifica a entrada se tiver virgula troca por float
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            #isalpha() Esta função é usada para verificar se o argumento inclui apenas caracteres do alfabeto
            #O "strip ()" retira os espaços em branco
            print(f'O VALOR PARA PESO:\"{entrada}\" NÃO É VALIDO!!')
        else:
            valido = True
            return float(entrada)


def total(a=0, b=0, c=0):
    #Def usada para fazer o calculo das dimensões do produto
    try:
        total1 = a * b *c
        if total1 > 100000:
            print('')
        return total1
    except ValueError:
        print('Valor inválido para Calculo')

def valorapagar(a=0, b=0, c=0):
    #utilizada para calcular o valor á ser pago
    valp3993994 = a * b * c
    return valp3993994

#Programa Principal

borda('Bem vindo a Companhia de logistica Isaias Batista RU:3993994')
#Utilizado a def borda
while True:
    comprimento = InteiroRU3993994('Digite o comprimento do objeto (em cm³): ')
    # função verificar se é valor númerico Ru3993994
    largura = InteiroRU3993994('Digite a largura do objeto (em cm³): ')
    # função verificar se é valor númerico Ru3993994
    altura = InteiroRU3993994('Digite o altura do objeto (em cm³): ')
    # função verificar se é valor númerico Ru3993994
    dimencoes = total(comprimento, largura, altura)
    print(f'O volume do objeto é (cm³): {dimencoes:.2f}')
    #Calcula as dimensões
    if dimencoes <= 100000:
        break
    else:
        print('NÃO ACEITAMOS OBJETOS COM DIMENSÕES TÃO GRANDES')
        continue
custo = dimencoes
#Custo das dimencoes dos produtos.
if custo <= 1000:
    custo = 10
elif custo or 1001 or custo or 10000:
    custo = 20
elif custo or 10001 or custo or 30000:
    custo = 30
else:
    print('NÃO ACEITAMOS OBJETOS COM DIMENSÕES TÃO GRANDES')
try:
#Verificar se o peso é menor que 30kg e o valor é numérico.
    while True:
        peso = validapeso('Qual é o peso do objeto (em kg): ')
        if peso <= 30:
            break
        else:
            print('NÃO ACEITAMOS OBJETOS COM PESO MAIOR QUE 30Kg ')
            continue
except:
    print('Valor inválido!!')
#variável para reseceber o peso
custopeso = peso
#Custo do peso segundo a tabela de conversão
if custopeso <= 0.1:
    custopeso = 1
elif custopeso <= 0.11:
    custopeso = 1.5
elif custopeso <= 1:
    custopeso = 1.5
elif custopeso <= 1.10:
    custopeso = 2
elif custopeso <= 10:
    custopeso = 2
elif custopeso <= 10.1:
    custopeso = 2
elif custopeso <= 10.1:
    custopeso = 2
elif custopeso <= 30:
    custopeso = 3
print('**'*32)
print('Selecione uma rota\n\nJC- De Joaçaba  até Chapecó\nJR - De Joaçaba até Rio do sul\nJB - De  Joaçaba até '
      'Blumenau')
print('**'*32)#Escolher a rota para o preço final.
while True:
    rota = str(input('Selecione uma rota válida : ').upper()).strip()
    #Função do python upper() e strip() para colocar em maiúscula e remover espaços vazios.
    if rota == "JC":
        rota = valorapagar(custo, custopeso, 1)
        print(f'O total á pagar é: R$ {rota:.2f} (dimensões {custo} * peso {custopeso} * rota 1)')
        break
    elif rota == "JR":
        rota = valorapagar(custo, custopeso, 1)
        print(f'O total á pagar é: R$ {rota:.2f} (dimensões {custo} * peso {custopeso} * rota 1)')
        break
    elif rota == "JB":
        rota = valorapagar(custo, custopeso, 1.2)
        print(f'O total á pagar é: R$ {rota:.2f} (dimensões {custo} * peso {custopeso} * rota 1.2)')
        break
    else:
        print('Você digitou um rota que não existe!!!')
        continue
print('Desvenvolvedor Isaias Batista RU:3993994')
