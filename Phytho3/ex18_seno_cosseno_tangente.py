import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print(f'O ângulo {ângulo} tem o seno de {seno:.2f}')
coseno = math.cos(math.radians(ângulo))
print(f'O ângulo {ângulo} tem do coseno de {coseno:.2f}')
tangente = math.tan(math.radians(ângulo))
print(f'O ângulo {ângulo} tem a tangente de {tangente:.2f}')
