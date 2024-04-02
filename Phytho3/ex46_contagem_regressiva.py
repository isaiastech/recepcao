from time import sleep
print('......INCIANDO A CONTAGEM.....')
for cont in range(0, 11).__reversed__():
    sleep(1)
    print(f'{cont}'.center(20))
sleep(1)
print('BUM!! BUM!! BUM!! BUM!!')
