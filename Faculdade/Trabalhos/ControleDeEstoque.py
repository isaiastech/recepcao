# -*- encoding: utf-8 -*-
def borda(msg: str) -> str: #Type Annotation para declaração de variáveis usado a partir do python 3
#Código copiado da aula de funções do  Prof. Me. Eng. Renan Portela Jorge.
    titulo = len(msg)
    if titulo:
        print('+', '-' * titulo,'+')
        print('|', msg, '|')
        print('+', '-' * titulo,'+')
def cadastraPeca():
    dados=



#Programa principal
borda('Bem vindo ao Controle de Estoque da Bicicletaria do Isaias Batista RU:3993994')
print('Escolha a opção desejada: ')
print('1 - Cadastrar Peças\n2 - Consultar Peças\n3 - Remover Peças\n4 - Sair')

