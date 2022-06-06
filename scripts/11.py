##
## automates the task of ipiranga
## 

# import the py libraries and files
import pyautogui
import time
from datetime import date
from variables import *
from methods import *

# portal ipiranga
noteBook() #check which laptop is in use
yesterday = getDateYesterday() #take yesterday's date
runBrave() #start the browser brave
runUrl(linkIpiranga) #type the url

# login portal ipiranga
pyautogui.click(ipirangaLogin) #click login
time.sleep(5)
pyautogui.write(loginIpiranga) #type login
time.sleep(2)
pyautogui.press('tab') #change between fields
pyautogui.write(passwordIpiranga) #type password
pyautogui.press('enter') #confirm entry
time.sleep(30)

# closed pop up
pyautogui.click(ipirangaClosedPopUp) #click on "fechar pop up"
time.sleep(2)

# print values
pyautogui.click(ipirangaRequests) #click on "pedidos"
time.sleep(10)
printImg = pyautogui.screenshot('15-IpirangaValues.png') #generate print

# closed pop up
pyautogui.click(ipirangaClosedPopUp) #click on "fechar pop up"
time.sleep(2)

# print tickets
time.sleep(5)
pyautogui.click(ipirangaStart) #click on "pagina inicial"
time.sleep(20)
pyautogui.click(ipirangaTickets) #click on "boletos"
time.sleep(20)
pyautogui.press('down', presses=25) #move the screen down #did not work?
time.sleep(2)
printImg = pyautogui.screenshot('16-IpirangaDuplicates.png') #generate print

closedBrave()
