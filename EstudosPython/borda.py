from datetime import datetime
hora = datetime.now()
hora = hora.strftime('%d-%m-%Y ')
resumo = 'RESUMO DO CAIXA'
print('+', '-' *len(resumo + hora) , '+' )
print('|', resumo, hora,'|')
print('+', '-' *len(resumo + hora),'+')
