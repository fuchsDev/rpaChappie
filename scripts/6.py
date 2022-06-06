##
## automates the task of linx seller
## 

# import the py libraries and files
import pyautogui
import time
from datetime import date
from variables import *
from methods import *

# linx seller web 'descontos'
noteBook() #check which laptop is in use 
yesterday = getDateYesterday() #take yesterday's date
runBrave() #start the browser brave
runUrl(linkLinx) #type the url 
runLinxNewTab() #call method open newtab with linxseller in methods.py
loginLinxSeller(loginLinx, passwordLinx) #send variables to method in methods.py
zoomIn() #zoom in brave to adjust menu position

# print 'descontos'
pyautogui.moveTo(linxConsultMenu) #click on 'menu consultas'
time.sleep(2)
pyautogui.moveTo(linxMenuAudit) #move to / click on 'auditoria'
time.sleep(2)
pyautogui.moveTo(linxMenuChanges) #click on 'alteracao ingredientes'
time.sleep(2)
pyautogui.moveTo(linxMenuSales) #move to
time.sleep(2)
pyautogui.click(linxMenuSales) #click on 'vendas por documento fiscal'   
time.sleep(10)
pyautogui.click(linxDiscountDateField) #click on 'campo data desconto'
time.sleep(2)
pyautogui.write(yesterday) #write yesterday's date in the field
time.sleep(2)
pyautogui.press('tab') #press key
time.sleep(1)
pyautogui.press('tab') #press key
time.sleep(2)
pyautogui.write(yesterday) #write yesterday's date in the field
time.sleep(2)
pyautogui.moveTo(linxDiscountBox) #move to
time.sleep(2)
pyautogui.click(linxDiscountBox) #click on 'caixa apenas desconto'
time.sleep(1)
pyautogui.click(linxDescountClient) #click on 'campo cliente'
time.sleep(1)
pyautogui.write('consumidor final') #type 'consumidor'
time.sleep(2) 
pyautogui.click(linxDicountOk) #click on 'ok'
time.sleep(10)

zoomOut() #zoom out in brave to adjust menu position
pyautogui.press('down', presses=5) #press key to adjust screen
printImg = pyautogui.screenshot('07-LinxDiscount.png') #generate print

closedBrave() #closed tab the browser brave
closedBrave() #closed tab the browser brave