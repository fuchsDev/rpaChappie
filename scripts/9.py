## verificar os preços e as duplicatas no portal cs online shell

from methods import *

# verifica o notebook / acessa o brave / digita o link
noteBook() 
runBrave() 
runUrl(linkShell) 

# login cs online
pyautogui.click(shellLogin)
time.sleep(5)
pyautogui.write(loginShell) 
time.sleep(2)
pyautogui.press('tab') 
pyautogui.write(passwordShell) 
pyautogui.press('enter') 
time.sleep(10)
pyautogui.click(shellSelecionaCombustiveisClaros) 
time.sleep(20)

# verifica os valores para pedido com 10 dias
pyautogui.moveTo(shellPedidos) 
time.sleep(2)
pyautogui.moveTo(shellIngressarPedidos) 
time.sleep(2)
pyautogui.click(shellIngressarPedidos) 
time.sleep(45)
printImg = pyautogui.screenshot('11-ShellValoresCombustiveis.png')
time.sleep(2)

# verificar duplicatas em aberto no financeiro
pyautogui.moveTo(shellFinanceiro) 
time.sleep(2)
pyautogui.moveTo(shellFinanceiroExtratoContas) 
time.sleep(2)
pyautogui.click(shellFinanceiroExtratoContas) 
time.sleep(20)

printImg = pyautogui.screenshot('12-ShellDuplicatas.png')
closedBrave()