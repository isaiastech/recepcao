from utilitarios import cores
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua Altura? '))
IMC = peso / (altura ** 2)
cores.verde(f'O IMC dessa pessoa é de {IMC:.3f}')
if IMC <= 18.5:
    cores.vermelho('VOCÊ ESTÁ ABAIXO DO PESO')
elif 18.5 <= IMC <= 24.9:
    cores.verde('PESO NORMAL')
elif 24.9 >= IMC <= 30:
    cores.amarelo('SOBREPESO')
elif IMC >= 30 < 34.9:
    cores.azul('OBESIDADE GRAU 1')
elif IMC >= 34.9 < 39.9:
    cores.MagentaClaro('OBESIDADE GRAU 2')
else:
    cores.vermelho('OBESIDADE GRAU 3 VOCÊ ESTÁ EM OBESIDADE MÓRBIDA')


# IMC	Resultado
# Menos do que 18,5	Abaixo do peso
# Entre 18,5 e 24,9	Peso normal
# Entre 25 e   29,9	Sobrepeso
# Entre 30 e   34,9	Obesidade grau 1
# Entre 35 e   39,9	Obesidade grau 2
# Mais do que  40	Obesidade grau 3
