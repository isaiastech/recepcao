import calendar

calendario = int(input('Digite um ano e veja seu calendario: '))
calendario = (calendar.TextCalendar(calendar.SUNDAY).formatyear(calendario))
print(calendario)
