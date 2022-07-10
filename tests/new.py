#
# remember billing dates
#

# criar um aviso de faturamentos de clientes por dia conforme agenda
# pensar na situação de feriados e final de semana

'''
Ideias de novas funcionalidades:
- lembretes dos clientes que tem faturamento agendado para o dia (Auto Posto);
- fechamento dos PDVs pelo Compusis Web (3817);
- rotina de LMC Compusis Web (3779);
- download de relatórios mensais usados no DRE Gerencial;
- print dos produtos cadastrados no dia anterior nos sistemas Linx e Compusis;
- verificar se planilha de cobranças dos clientes foi atualizada;
- conciliar inventários utilizando arquivos .txt;
- elaborar escalas dos funcionários (Auto Posto);
- calcular e projetar o mês de recebimento de bônus contratual;
- refatorar e limpar o código (simplificar);
'''

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