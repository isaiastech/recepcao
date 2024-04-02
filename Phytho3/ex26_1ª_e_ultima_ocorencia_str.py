#026 - Primeira e última ocorrência de uma string
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A {} aparce na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A') +1))
print('A letra A aparece a última vez {}'.format(frase.rfind('A')+ 1))
