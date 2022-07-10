##
## rotina inicio de dia no sistema compusis fl01
## 

import pyautogui
import time
from variables import *
from methods import *

noteBook() #check which laptop is in use 
runBrave() #start the browser brave
runUrl(linkCompusisFl01) #type the url 
loginCompusis(loginCompusisFl01, passwordCompusisFl01) #send variables to method in methods.py

# select branch fl01
pyautogui.click(compusis01Company) #click on company position
time.sleep(5)
pyautogui.click(compusis01Branch) #click on branch position
time.sleep(5)
pyautogui.click(compusis01Enter) #click enter
time.sleep(10)

run1908() #call method that is in methods.py
printImg = pyautogui.screenshot('02-CompusisIpiranga1908.png') #generate print
closedBrave()

run1980() #call method that is in methods.py
printImg = pyautogui.screenshot('03-CompusisIpiranga1980.png') #generate print
closedBrave()

closedBrave()
