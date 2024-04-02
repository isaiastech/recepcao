"""print(5+6+9)
print((23+19+31)/3)
print(403//73)
print(403%73)
print(2**10)
print(min(34,29,31))
a = 3
b = 4
c = (a * a) + (b * b)
print(c)
s1='ant'
s2= 'bat'
s3= 'cod'
print(f"{s1} {s2} {s3}")
print(f'{s1*10}')"""""

produto = float(input('Qual o preço do produto? '))
desconto = float(input('Qual o valor do desconto? '))
resp = (produto * desconto )/100
valorfinal = produto - resp
print(f'O produto que custava R${produto} com o desconto de {desconto}% \n'
      f'ficará no valor de R${valorfinal}')
