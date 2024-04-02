print('='*30)
print('PROGRESSÃO ARITIMÉTICA'.center(30))
print('='*30)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
Décimo = primeiro + (10 -1) * razão
for c in range(primeiro, Décimo + razão, razão):
    print(f'{c}', end=' -> ')
print('ACABOU')
