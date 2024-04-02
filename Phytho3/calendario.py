import calendar
from utilitarios import cores
from datetime import date
data = date.today().year
mes = (calendar.TextCalendar(calendar.SUNDAY))
mes.prmonth(2020, 10)
calendario = int(input('Digite o ano e veja seu calendário: '))
calendario = (calendar.TextCalendar(calendar.SUNDAY).formatyear(calendario))
cores.azul(calendario)


