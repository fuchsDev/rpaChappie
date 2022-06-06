##
## automates the task of linx seller
## 

# import the py libraries and files
import pyautogui
import time
from variables import *
from methods import *

# linx seller 'suprimentos'
noteBook() #check which laptop is in use 
yesterday = getDateYesterday() #take yesterday's date
runBrave() #start the browser brave
runUrl(linkLinx) #type the url
runLinxNewTab() #call method open newtab with linxseller in methods.py
loginLinxSeller(loginLinx, passwordLinx) #send variables to method in methods.py

zoomIn() #zoom in brave to adjust menu position

# download .xlxs
pyautogui.moveTo(linxConsultMenu) #click on 'menu consultas'
time.sleep(3)
pyautogui.moveTo(linxMenuTreasury) #click on 'menu tesouraria'   
time.sleep(3)        
pyautogui.moveTo(linxMenuChangesPayment) #click on 'alteracoes forma de pagamento'     
time.sleep(3)        
pyautogui.moveTo(linxMenuBleedsSupplies) #move to on 'sangrias e suprimentos' 
time.sleep(3)
pyautogui.click(linxMenuBleedsSupplies) #click on 'sangrias e suprimentos'
time.sleep(10)

zoomOut() #zoom out in brave to adjust menu position

pyautogui.click(linxSuplliesData01) #click on 'data 1 dos suprimentos'
time.sleep(3)
pyautogui.write(yesterday) #type yesterday date
time.sleep(3)
pyautogui.click(linxSuppliesData02) #click on 'data 2 dos suprimentos'
time.sleep(3)
pyautogui.write(yesterday) #type yesterday date
time.sleep(3)
pyautogui.click(linxSuppliesOk) #click on 'ok'
time.sleep(3)
pyautogui.click(linxSuppliesDownload) #click on 'download'
time.sleep(3)
pyautogui.click(linxSuppliesSave) #click on 'save'
time.sleep(10)
pyautogui.click(braveClosedDownload) #close bottom bar Download
time.sleep(5)

closedBrave()
closedBrave()