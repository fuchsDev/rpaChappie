##
## automates the task of verifying the functioning of the solar energy system
## 

# import the py libraries and files
import pyautogui
import time 
from variables import *
from methods import *

# solarView methods
noteBook() #check which laptop is in use 
runBrave() #start the browser brave 
runUrl(linkSolarView) #type the url 

# login solarView  
pyautogui.click(solarInsertEmail) #click on the position to enter email
time.sleep(2) 
pyautogui.write(loginSolarView) #write login
time.sleep(2)
pyautogui.press('tab')
pyautogui.write(passwordSolarView) #write password
time.sleep(2)
pyautogui.click(solarCaptcha) #select captcha "I'm not a robot"
time.sleep(5)
pyautogui.click(solarLogin) #click enter
time.sleep(45)
printImg = pyautogui.screenshot('01-SolarView.png') #generate print

# logout solarView
time.sleep(2)
pyautogui.click(solarProfile) #click profile
time.sleep(2)
pyautogui.click(solarExit) #select exit

closedBrave()
