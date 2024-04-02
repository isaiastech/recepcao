número = int(input('Digite um número para ver sua tabuada: '))
print('-='*20)
for tab in range(1, 11):
    print(f'{número} X {tab} = {tab * número}')
print('-='*20)
