##
## automates the task of compusis
## 

# import the py libraries and files
import pyautogui
from variables import *
from methods import *

# compusisWeb Fl02 methods
noteBook() #check which laptop is in use 
runBrave() #start the browser brave
runUrl(linkCompusisFl02) #type the url 
loginCompusis(loginCompusisFl02, passwordCompusisFl02) #send variables to method in methods.py

run1908() #call method that is in methods.py
printImg = pyautogui.screenshot('04-CompusisShell1908.png') #generate print
closedBrave() #call method that is in methods.py /closed tab

run1980() #call method that is in methods.py
printImg = pyautogui.screenshot('05-CompusisShell1980.png') #generate print
closedBrave() #call method that is in methods.py

closedBrave()