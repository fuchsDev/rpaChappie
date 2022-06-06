##
## methods used in scripts
## 

# import the py libraries and files
import pyautogui
import time 
import datetime
import socket
from datetime import date
from variables import * 

# method check laptop
noteName = socket.gethostname()
if noteName == 'fk-Aspire-A315-56':
    from positionsIntel import *
else:
    from positionsAmd import *


def noteBook():
    noteName = socket.gethostname()
    if noteName == 'fk-Aspire-A315-56': 
        #from positionsIntel import *
        import positionsIntel as positionsIntel
    else:
        #from positionsAmd import *
        import positionsAmd as positionsAmd

# method zoom in and out
def zoomIn():
    if noteName == 'fk-Aspire-A315-56':
        #intel ctrl + x2 zoon in 100%
        time.sleep(15)
        pyautogui.hotkey('ctrl', '+')
        pyautogui.hotkey('ctrl', '+')
    else:
        #amd Zoom Ok
        time.sleep(2)

def zoomOut():
    if noteName == 'fk-Aspire-A315-56':
        #intel ctrl - x2 zoom out 80%
        time.sleep(15)
        pyautogui.hotkey('ctrl', '-')
        pyautogui.hotkey('ctrl', '-')
    else:
        #amd zoom Ok
        time.sleep(2)


# brave browser
def runBrave():
    pyautogui.click(braveStart)
    time.sleep(5)

def closedBrave():
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('f4')
    pyautogui.keyUp('ctrl')

def runUrl(link):
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    pyautogui.write(link)
    pyautogui.press('enter')
    time.sleep(10)

# yesterday
def getDateYesterday():
    date_now = datetime.datetime.now()
    one_days_ago = date_now - datetime.timedelta(days=1)
    yesterday = one_days_ago.strftime("%d/%m/%Y")
    return yesterday

# compusis web   
def loginCompusis(login, password): #receives variables login and password sent by 1.py
    pyautogui.click(compusisUser) #click on the user position
    time.sleep(5)
    pyautogui.write(login)
    pyautogui.press('tab')
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(10)

def run1908(): #flags
    pyautogui.keyDown('ctrl')
    pyautogui.press('g')
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    pyautogui.write('1908')
    time.sleep(2)
    pyautogui.press('down', presses=2)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(compusisSearchFlags)
    time.sleep(10)
    pyautogui.click(compusisRun)
    time.sleep(10)

def run1980(): #open day
    pyautogui.keyDown('ctrl')
    pyautogui.press('g')
    pyautogui.keyUp('ctrl')
    pyautogui.write('1980')
    pyautogui.press('down', presses=2)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.click(compusisRun)
    time.sleep(10)

# linx seller
def runLinxNewTab():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.click(linxNewTab) #click on open new tab button 'linx seller'
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    time.sleep(5)

def loginLinxSeller(login, password):
    pyautogui.click(linxUser) #click on 'usuario linx'
    time.sleep(5)
    pyautogui.write(login)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(linxConnect) #click on 'conectar tela inicial linx'
    time.sleep(10)
    pyautogui.click(linxMatriz) #click on 'escolhe matriz linx seller'
    time.sleep(5)