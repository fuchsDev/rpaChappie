## verifica chamados e duplicatas no portal linx cliente

from methods import *

# verifica o notebook / acessa o brave e digita o link
noteBook()
runBrave()
runUrl(linkLinxPortal) 

# login portal linx web #o login pode ser um metodo igual os outros
pyautogui.click(portalLinxUsuario) 
time.sleep(5)
pyautogui.write(loginLinxPortal) 
time.sleep(2)
pyautogui.press('tab') 
pyautogui.write(passwordLinxPortal) 
pyautogui.press('enter') 
time.sleep(5)
pyautogui.click(portalLinxEnviar) 
time.sleep(60)

# verificar chamados em aberto no suporte
pyautogui.moveTo(portalLinxMenuSuporte) 
time.sleep(2)
pyautogui.click(portalLinxMenuSuporte) 
time.sleep(2)
pyautogui.moveTo(portalLinxPainelChamados) 
time.sleep(2)
pyautogui.click(portalLinxPainelChamados) 
time.sleep(10)
printImg = pyautogui.screenshot('09-LinxPortalChamados.png')
time.sleep(2)

# verifica duplicatas a pagar
pyautogui.moveTo(portalLinxMenuFinanceiro)
time.sleep(2)
pyautogui.click(portalLinxMenuFinanceiro)
time.sleep(2)
pyautogui.moveTo(portalLinxFinanceiroFaturas) 
time.sleep(2)
pyautogui.click(portalLinxFinanceiroFaturas) 
time.sleep(30)
pyautogui.moveTo(portalLinxFinanceiroSeta) 
time.sleep(2)
pyautogui.click(portalLinxFinanceiroSeta)
time.sleep(10)
pyautogui.moveTo(portalLinxFinanceiroEmpresa)
time.sleep(2)
pyautogui.click(portalLinxFinanceiroEmpresa) 
time.sleep(20)

printImg = pyautogui.screenshot('10-LinxPortalDuplicatas.png')
closedBrave()