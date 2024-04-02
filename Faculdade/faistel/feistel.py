import binascii
import operator

def rand_key(p) :
    key1 = ""
    p = int(p)

    for i in range(p) :
        # Final da minha RU; Univirtus utlizado para gerar chave criptográfica
        temp = int(4)
        temp = str(temp)
        key1 = key1 + temp

    return (key1)


def exor(a, b) :
    temp = ""

    for i in range(n) :
        if (a[i] == b[i]) :
            temp += "0"
        else :
            temp += "1"

    return temp


def BinaryToDecimal(binary) :
    string = int(binary, 2)

    return string
#PT significa texto plano.
PT = "Isai"
print("O Texto Plano é:", PT)
#Pega cada letra  posicão do texto plano na tabela tabela ASCII
PT_Ascii = [ord(x) for x in PT]
# converte o texto plano em Binário
PT_Bin = [format(y, '08b') for y in PT_Ascii]
#Junta todos os binários
PT_Bin = "".join(PT_Bin)
#Divide os binários em duas partes
n = int(len(PT_Bin) // 2)
L1 = PT_Bin[0 :n]
R1 = PT_Bin[n : :]
m = len(R1)

K1 = rand_key(m)

K2 = rand_key(m)
# XOR de R1, K1
f1 = exor(R1, K1)
# XOR de F1, L1
R2 = exor(f1, L1)
L2 = R1
# Operações XOR
f2 = exor(R2, K2)
R3 = exor(f2, L2)
L3 = R2

bin_data = L3 + R3
str_data = ' '

for i in range(0, len(bin_data), 7) :
    temp_data = bin_data[i :i + 7]

    decimal_data = BinaryToDecimal(temp_data)

    str_data = str_data + chr(decimal_data)

print("Texto codificado:", str_data)
L4 = L3
R4 = R3
# Operações XOR
f3 = exor(L4, K2)
L5 = exor(R4, f3)
R5 = L4
# Operações XOR
f4 = exor(L5, K1)
L6 = exor(R5, f4)
R6 = L5
PT1 = L6 + R6

PT1 = int(PT1, 2)
RPT = binascii.unhexlify('%x' % PT1)
print("Recuperado é: ", RPT)
