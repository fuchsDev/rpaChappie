##
## automates the task of vibra
## 

# import the py libraries and files
import pyautogui
import time
from datetime import date
from variables import *
from methods import *

# vibra distribuidora
noteBook() #check which laptop is in use 
yesterday = getDateYesterday() #take yesterday's date
runBrave() #start the browser brave
runUrl(linkVibra) #type the url 

# login
pyautogui.click(vibraLogin) #click on the login  
time.sleep(5)
pyautogui.write(loginVibra) #type loginVibra of variables.py
time.sleep(2)
pyautogui.press('tab') #press key
pyautogui.write(passwordVibra) #type password of variables.py
pyautogui.press('enter') #press key
time.sleep(20)

### IS NOT WORKING ###
#pyautogui.click(vibraClosedPopUp, clicks=5, interval=0.5) #closed 'Pop Ups'
#time.sleep(10)
### IS NOT WORKING ###


# print financeiro
#pyautogui.moveTo(vibraPay) #move x, y, time in seconds
#time.sleep(2)
pyautogui.click(vibraPay) #click on bill pay
time.sleep(20)
pyautogui.press('down', presses=15) #press key
time.sleep(5)
printImg = pyautogui.screenshot('14-VibraDubplicates.png') #generate print
time.sleep(2)
pyautogui.press('up', presses=15) #press key

# print valores em visao geral
pyautogui.click(vibraOverview) #click on 'visao geral'
pyautogui.click(vibraOverview) #you need to click twice
time.sleep(20)
pyautogui.press('down', presses=15) #press key
time.sleep(2)
printImg = pyautogui.screenshot('13-VibraValues.png') #generate print
time.sleep(2)

closedBrave()