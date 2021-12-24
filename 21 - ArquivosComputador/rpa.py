import pyautogui as py

py.PAUSE = 2
py.press('win')
py.write('chrome')
py.press('enter')
py.write('gmail')
py.press('enter')

#reconhecimento de imagem
x, y, largura, altura = py.locateOnScreen('google.PNG')
#clicar no meio da imagem
py.click(x + largura/2, y + altura/2)