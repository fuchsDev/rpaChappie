##
## automates the task of linx seller
## 

# import the py libraries and files
import pyautogui
import time
from datetime import date
from variables import *
from methods import *

# linx seller 'afericoes'
noteBook() #check which laptop is in use 
yesterday = getDateYesterday() #take yesterday's date
runBrave() #start the browser brave
runUrl(linkLinx) #type the url 
runLinxNewTab() #call method open newtab with linxseller in methods.py
loginLinxSeller(loginLinx, passwordLinx) #send variables to method in methods.py
zoomIn() #zoom in brave to adjust menu position

# print
pyautogui.moveTo(linxConsultMenu) #click on 'menu consultas'
time.sleep(2)
pyautogui.moveTo(linxMenuInventory) #click on 'menu estoque'
time.sleep(2)
pyautogui.moveTo(linxMenuSpin) #click on 'menu giro'
time.sleep(2)
pyautogui.moveTo(linxMenuMoviment) #click on 'movimentacao gerencial'
pyautogui.click(linxMenuMoviment) #click on 'movimentacao gerencial'
time.sleep(10)
pyautogui.click(linxDataScounting) #click on 'campo data afericao'
time.sleep(1)
pyautogui.press('backspace', presses=10) #press the key to erase
time.sleep(2)
pyautogui.write(yesterday) #type yesterday date
time.sleep(2)
pyautogui.press('tab') #press the key to switch fields
time.sleep(1)
pyautogui.press('tab') #press the key to switch fields
time.sleep(2)
pyautogui.write(yesterday) #type yesterday date
time.sleep(2)
pyautogui.click(linxEmptyScounting) #click on 'vazio'
time.sleep(2)
pyautogui.press('down', presses=15) #press the key to go down
time.sleep(2)
pyautogui.click(linxOperationsScouting) #click on 'operacocoes em afericoes'
time.sleep(2)
pyautogui.moveTo(linxScoutingScounting) #move to on 'afericoes em afericoes'
time.sleep(2)
pyautogui.click(linxScoutingScounting) #click on 'afericoes em afericoes'
time.sleep(2)
pyautogui.click(linxEmptyScountiTwo) #click on 'vazio'
time.sleep(2)
pyautogui.click(linxToApplyScounting) #click on 'aplicar'
time.sleep(10)

zoomOut() #zoom out in brave to adjust menu position
printImg = pyautogui.screenshot('08-LinxScounting.png') #generate print

closedBrave()
closedBrave()