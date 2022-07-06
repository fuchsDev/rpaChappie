##
## automates the task of linx seller
## 

# import the py libraries and files
import pyautogui
import time
from variables import *
from methods import *

# linx seller web 'fechar cxs'
noteBook() #check which laptop is in use 
runBrave() #start the browser brave
runUrl(linkLinx) #type the url  
runLinxNewTab() #call method open newtab with linxseller in methods.py
loginLinxSeller(loginLinx, passwordLinx) #send variables to method in methods.py

# check shifts
#pyautogui.click(linxShortcurtClosedCx) #shift check shortcut



'''
criar novas variaveis 
X:  212 Y:  217 operacoes
X:  212 Y:  408 tesouraria 
X:  510 Y:  406 alteracao forma de pagamento
X:  497 Y:  504 conferencia de turno
'''



time.sleep(10)
pyautogui.click(linxOpenCx) #Click on the open cashier on the right
time.sleep(10)
pyautogui.click(linxClosedN) #Click Closed Cx's position - 'none closed'
time.sleep(2)
pyautogui.click(linxClosedA) #Click Closed Cx's position - 'when it has already closed'
time.sleep(15)
pyautogui.click(linxConfirmClose) #Click confirm close 1
time.sleep(15)
pyautogui.click(linxConfirmClose) #Click Confirma close 2
time.sleep(15)

printImg = pyautogui.screenshot('06-LinxPDV.png') #generate print
closedBrave()