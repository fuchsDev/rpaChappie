## rotina inicio de dia no sistema compusis fl01

from methods import *
from variables import *

# verifica o notebook / acessa o brave e digita o link
noteBook() 
runBrave() 
runUrl(linkCompusisFl01) 

# metodo para login no compusis web
loginCompusis(loginCompusisFl01, passwordCompusisFl01)

# seleciona filial 01 para entrar
pyautogui.click(compusis01Empresa)
time.sleep(5)
pyautogui.click(compusis01Filial)
time.sleep(5)
pyautogui.click(compusis01Enter) 
time.sleep(10)

# executa rotina de verificar bandeira e abrir dia do movimento
run1908() 
printImg = pyautogui.screenshot('02-CompusisIpiranga1908.png')
closedBrave()
run1980() 
printImg = pyautogui.screenshot('03-CompusisIpiranga1980.png')
closedBrave()

closedBrave()