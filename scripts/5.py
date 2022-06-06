##
## automates the task of linx seller
## 

# import the py libraries and files
import pyautogui
import time 
from variables import *
from methods import *

# linx seller 'recebimentos'
noteBook() #check which laptop is in use 
yesterday = getDateYesterday() #take yesterday's date
runBrave() #start the browser brave
runUrl(linkLinx) #type the url 
runLinxNewTab() #call method open newtab with linxseller in methods.py
loginLinxSeller(loginLinx, passwordLinx) #send variables to method in methods.py

# download .xlxs
pyautogui.click(linxShortcutReceiving) #shortcut receipts    
time.sleep(15)
pyautogui.click(linxReceivingDate) #select date field
time.sleep(2)
pyautogui.write(yesterday) #type date yesterday
time.sleep(2)
pyautogui.press('tab') #press any key
time.sleep(2)
pyautogui.write(yesterday)  #type date yesterday
time.sleep(2)
pyautogui.click(linxDateOk) #ok search
time.sleep(5)
pyautogui.click(linxExpandReceipts) #click on the line to expand
time.sleep(3)
pyautogui.click(linxDownloadReceipts) #click download
time.sleep(3)
pyautogui.click(linxSaveReceipts) #click save file
time.sleep(10)
pyautogui.click(braveClosedDownload) #close bottom bar Download
time.sleep(5)

closedBrave()
closedBrave()