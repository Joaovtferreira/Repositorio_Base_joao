import pyautogui as p
from time import sleep


#p.mouseInfo()




p.press('win')
sleep(1)
p.write('chrome')
p.press('enter')
p.moveTo(957,578,duration=1)
p.click()
sleep(1)
p.write('https://term.ooo')
p.press('enter')
p.click()


#p.moveTo(792,280,duration=1)
#p.write('pioes')
#sleep(1)
#p.press('enter')
#sleep(1)
#p.moveTo(800,370)
#p.click()
#p.write('barco')