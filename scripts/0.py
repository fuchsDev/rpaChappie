##
## verifica o funcionamento dos paineis de energia solar;
##

import pyautogui
import time 
from variables import *
from methods import *

# verifica o notebook / acessa o brave e digita o link
noteBook() 
runBrave() 
runUrl(linkSolarView) 

# login solarView  
pyautogui.click(solarInsertEmail) 
time.sleep(2) 
pyautogui.write(loginSolarView) 
time.sleep(2)
pyautogui.press('tab')
pyautogui.write(passwordSolarView)
time.sleep(2)
pyautogui.click(solarCaptcha) #seleciona 'nao sou um robo'
time.sleep(5)
pyautogui.click(solarEntrar) 
time.sleep(45)
printImg = pyautogui.screenshot('01-EnergiaSolar.png')

# logout solarView
time.sleep(2)
pyautogui.click(solarPerfil)
time.sleep(2)
pyautogui.click(solarSair)

closedBrave()
