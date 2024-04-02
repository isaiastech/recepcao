print('-='*20)
print('Analisando Triângulo v1.0'.center(40))
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2= float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos náo podem formar um triângulo.')
