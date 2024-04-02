def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'COM {idade} ANOS VOCÊ NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'COM {idade} ANOS O VOTO É OPCIONAL'
    else:
        return f'COM {idade} ANOS O VOTO É OBRIGATÓRIO'

#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
