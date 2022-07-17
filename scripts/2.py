## rotina inicio de dia no sistema compusis fl02

from variables import *
from methods import *

# verifica o notebook / acessa o brave e digita o link
noteBook() 
runBrave() 
runUrl(linkCompusisFl02)

# metodo para login no compusis web
loginCompusis(loginCompusisFl02, passwordCompusisFl02) 

# executa rotina de verificar bandeira e abrir dia do movimento
run1908() 
printImg = pyautogui.screenshot('04-CompusisShell1908.png') 
closedBrave()
run1980() 
printImg = pyautogui.screenshot('05-CompusisShell1980.png') 
closedBrave() 

closedBrave()