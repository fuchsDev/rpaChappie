##
## automates the task of shell cs online
## 

# import the py libraries and files
import pyautogui
import time
from variables import *
from methods import *

# shell cs online
noteBook() #check which laptop is in use 
runBrave() #start the browser brave
runUrl(linkShell) #type the url

# login cs online
pyautogui.click(shellLogin) #click login
time.sleep(5)
pyautogui.write(loginShell) #type login of variables.py
time.sleep(2)
pyautogui.press('tab') #press key
pyautogui.write(passwordShell) #type password of variables.py
pyautogui.press('enter') #press key
time.sleep(10)
pyautogui.click(shellSelectFuel) #click on the 'combustiveis claros'
time.sleep(20)

# print prices
'''
pyautogui.click(shellClosedPopUp, clicks=5) #click for closed pop up's 
pyautogui.moveTo(shellPrices) #move x, y, time in seconds
time.sleep(2)
pyautogui.click(shellPrices) #click on the 'preços'
pyautogui.moveTo(shellInfo) #move x, y, time in seconds
time.sleep(2)
pyautogui.click(shellInfo) #click on the 'informacoes'
time.sleep(45)
printImg = pyautogui.screenshot('11-ShellValues.png') #generate print
time.sleep(2)
'''

# print prices 10 days
pyautogui.moveTo(shellRequests) #move x, y, time in seconds
time.sleep(2)
#pyautogui.click(shellRequests) #click on the 'pedidos'
pyautogui.moveTo(shellJoinRequests) #move x, y, time in seconds
time.sleep(2)
pyautogui.click(shellJoinRequests) #click on 'ingressar pedidos'
time.sleep(45)
printImg = pyautogui.screenshot('11-ShellValues10.png') #generate print
time.sleep(2)

# print financial
pyautogui.moveTo(shellFinancial) #move to 'financeiro'
time.sleep(2)
pyautogui.moveTo(shellAccountStatement) #move to 'extrato de contas'
time.sleep(2)
pyautogui.click(shellAccountStatement) #click on 'extrato de contas'
time.sleep(20)

printImg = pyautogui.screenshot('12-ShellDuplicates.png') #generate print
closedBrave()