times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {times[16:20]}')
print('-='*15)
print(f'Os times em ordem alfabética {sorted(times)}')
print('-='*15)
print(f'A chapecoense está na {times.index("Chapecoense")+1}ª posição')
