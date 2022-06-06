##
## automates the task of linx portal web
## 

# import the py libraries and files
import pyautogui
import time
from datetime import date
from variables import *
from methods import *

# linx portal web
noteBook() #check which laptop is in use 
yesterday = getDateYesterday() #take yesterday's date
runBrave() #start the browser brave
runUrl(linkLinxPortal) #type url of variables.py

# login portal linx web
pyautogui.click(portalLinxUser) #click on 'usuario' 
time.sleep(5)
pyautogui.write(loginLinxPortal) #type login of variables.py
time.sleep(2)
pyautogui.press('tab') #press key
pyautogui.write(passwordLinxPortal) #type password of variable.py
pyautogui.press('enter') #press key
time.sleep(5)
pyautogui.click(portalLinxSend) #click on 'enviar'
time.sleep(60)

# print support calls
pyautogui.moveTo(portalLinxSupport) #move x, y, time in seconds
time.sleep(2)
pyautogui.click(portalLinxSupport) #click on 'menu suporte'
time.sleep(2)
pyautogui.moveTo(portalLinxCalls) #move x, y, time in seconds
time.sleep(2)
pyautogui.click(portalLinxCalls) #click on 'menu painel de chamados'
time.sleep(10)
printImg = pyautogui.screenshot('09-LinxPortal01.png') #generate print
time.sleep(2)

# print financial
pyautogui.moveTo(portalLinxfinancial)
time.sleep(2)
pyautogui.click(portalLinxfinancial) #click on 'financeiro'
time.sleep(2)
pyautogui.moveTo(portalLinxAccounts) #move to on 'faturas'
time.sleep(2)
pyautogui.click(portalLinxAccounts) #click on 'faturas'
time.sleep(30)
pyautogui.moveTo(portalLinxArrow) #move to on 'seta'
time.sleep(2)
pyautogui.click(portalLinxArrow) #click on 'seta'
time.sleep(10)
pyautogui.moveTo(portalLinxCompany) #move to on 'empresa'
time.sleep(2)
pyautogui.click(portalLinxCompany) #click on 'empresa'
time.sleep(20)

printImg = pyautogui.screenshot('10-LinxPortal02.png') #generate print
closedBrave() #closed tab the browser brave