from datetime import date
ano = date.today().year
idade = int(input('Qual o ano de nascimento do atleta? '))
categoria = ano - idade
if categoria <= 9:
    print(f'O atleta que nasceu em {idade} tem {categoria} anos\nEstá na categoria MIRIN')
elif categoria <= 14:
    print(f'O atleta que nasceu em {idade} tem {categoria} anos\nEstá na categoria INFANTIL')
elif categoria <= 19:
    print(f'O atleta que nasceu em {idade} tem {categoria} anos\nEstá na categoria JUNIOR')
elif categoria <= 25:
    print(f'O atleta que nasceu em {idade} tem {categoria} anos\nEstá na categoria SÊNIOR')
else:
    print(f'O atleta que nasceu em {idade} tem {categoria} anos\nEstá na categoria MASTER')
