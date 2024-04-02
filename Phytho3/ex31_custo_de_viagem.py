#031 - Custo da Viagem
distancia = float(input('Qual a distancia de sua viagem? '))
print(f'Voçê está prestes a começar uma viagem de {distancia} Km.')
if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'Para sua viagem de {distancia} Km você vai pagar R$ {preço}')
