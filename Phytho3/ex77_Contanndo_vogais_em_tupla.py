from utilitarios.linhas import linhas
from utilitarios.mesnsagems_str import fimdoprograma
linhas()
palavras = ('APRENDER', 'PROGAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGAMADOR', 'FUTURO')
for p in palavras:
    print(f'\033[32m\nNa palavra {p.lower()} temos \033[32m', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;31m{letra}\033[32m', end=' ')
print(' ')
fimdoprograma(' ')
