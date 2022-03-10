import pyautogui
import pyperclip
import time


pyautogui.PAUSE = 1
yautogui.press('winleft')
# pyautogui.write('chrome')
# pyautogui.press('enter')
# #pyautogui.alert('Seja bem-vindo ao chrome!')
# pyautogui.hotkey('crtl', 't')

#
#  
# pyautogui.write('https://unitbrasil.unitplus.net/admin/')
# pyautogui.press('enter')



pyautogui.click(450,450);pyautogui.typewrite('graphicsnotes');pyautogui.press('enter')
time.sleep(2)
for i in range(107):
  pyautogui.press('right');pyautogui.press('enter')
  pyautogui.hotkey('ctrl','r');pyautogui.hotkey('ctrl','s')
  time.sleep(2)
  pyautogui.press('esc')
  time.sleep(2)
  time.sleep(2)