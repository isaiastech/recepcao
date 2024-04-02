# -*- encoding: utf-8 -*-
class pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def get_profissao(self):
        return self.profissao



p1 = pessoa("João", 30, 'Administrador')
p2 = pessoa("Paulo", 20, 'Recepcionista')
p3 = pessoa('Carlos', 38, 'Motorista')
p4 = pessoa('Rdrigo', 40, 'construtor')
print(f'O {p1.get_nome()} tem {p1.get_idade()} anos é {p1.get_profissao()}.')
print(f'O {p2.get_nome()} tem {p2.get_idade()} anos é {p2.get_profissao()}.')
print(f'O {p3.get_nome()} tem {p3.get_idade()} anos é {p3.get_profissao()}')
print(f'O {p4.get_nome()} tem {p4.get_idade()} anos é {p4.get_profissao()}')
