#
# remember billing dates
#

# criar um aviso de faturamentos de clientes por dia conforme agenda
# pensar na situação de feriados e final de semana

import datetime

clientShell = ""

def getDateYesterday():
    date_now = datetime.datetime.now()
    one_days_ago = date_now - datetime.timedelta(days=1)
    yesterday = one_days_ago.strftime("%d/%m/%Y")
    return yesterday

def getDateToday():
    dataNow = datetime.datetime.now()
    today = dataNow.strftime("%d/%m/%Y")
    return today

print (getDateToday())

def getDateTodayDay():
    dataNow = datetime.datetime.now()
    todayDay = dataNow.strftime("%d")
    return todayDay

print (getDateTodayDay())

from datetime import datetime
print(datetime.today().isoweekday()) #segunda feira comeca com 1

dayWeek = datetime.today().isoweekday()
print(dayWeek)

if dayWeek == 1:
    print("hoje é segunda feira, dia de faturar os clintes: ", clientShell )