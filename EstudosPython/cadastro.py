from  datetime import datetime
dia = datetime.today()
ext = dia.strftime('%d/%m/%Y')
print(ext)
nome = []
while True:
    incluir = str(input("Qual é seu nome: "))
    nome.append(incluir)
    escolha = str(input('Castrar mais alguém? (S \ N) ? ')).upper()
    if escolha == "N":
        break
    else:
        continue
print('Foram cadastrados:')
for i in nome:
    print(f'    {i}')
