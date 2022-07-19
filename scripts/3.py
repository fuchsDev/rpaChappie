## fechas os PDVs que estão em aberto do dia anterior

from methods import *

# verifica o notebook / acessa o brave / digita o link
noteBook() 
runBrave() 
runUrl(linkLinx) 

runLinxNewTab() 
loginLinxSeller(loginLinx, passwordLinx)

# acessa a tela de conferencia de turnos
pyautogui.click(linxMenuOperacoes)
time.sleep(3)
pyautogui.moveTo(linxOperacoesTesouraria)
time.sleep(3)
pyautogui.moveTo(linxOperacoesTesourariaAlteracao)
time.sleep(3)
pyautogui.click(linxOperacoesTesourariaAlteracaoConferenciaTurno)
time.sleep(10)
pyautogui.click(linxTurnosCaixasAberto) 
time.sleep(10)
pyautogui.click(linxTurnosFechaPDVN)
time.sleep(2)
pyautogui.click(linxTurnosFechaPDVA)
time.sleep(15)
pyautogui.click(linxTurnosCaixasConfirmaFechar) 
time.sleep(15)
pyautogui.click(linxTurnosCaixasConfirmaFechar)
time.sleep(15)

printImg = pyautogui.screenshot('06-LinxPDV.png')
closedBrave()