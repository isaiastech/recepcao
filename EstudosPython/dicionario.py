lanchonete = {"Salgado" : 4.50,"Lanche" : 3.60, "Suco" : 3.00,
              "Refrigerante" : 3.50, "Doce" : 1.50  }


for produto, preco in lanchonete.items():
    print(f'{produto:.<20}R$ {preco:.2f}')
print('-=' * 20)

for prod, preco in lanchonete.items():
    print(f'{prod:.<30} R${preco:.2f}')
print(lanchonete.values())
print(lanchonete)

cont = 0
codigo = 0
while (cont <= 13):
    codigo = cont
    cont += 2
    print(f'{cont:.<10}  código:{codigo}')

for menu, valor in lanchonete.items():
    print(f'{menu} {valor}')

