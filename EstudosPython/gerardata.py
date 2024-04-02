from datetime import date

def data():
    meses = ['Janeiro', 'fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    try:
        data_atual = date.today()
        dia = data_atual.strftime('%d')
        mes = data_atual.strftime('%m')
        ano = data_atual.strftime('%Y')
        if mes == '01':
            mes = meses[0]
        elif mes == '02':
            mes = meses[1]
        elif mes == '03':
            mes = meses[2]
        elif mes == '04':
            mes = meses[3]
        elif mes == '05':
            mes = meses[4]
        elif mes == '06':
            mes = meses[5]
        elif mes == '07':
            mes = meses[6]
        elif mes == '08':
            mes = meses[7]
        elif mes == '09':
            mes = meses[8]
        elif mes == '09':
            mes = meses[9]
        elif mes == '10':
            mes = meses[10]
        elif mes == '11':
            mes = meses[11]
        else:
            mes == meses[12]
        print('')
        print(f'{dia} de {mes} de {ano}')

    except:
        print('Algo de errado aconteceu')

#Programa Principal
data()


