import pyautogui
files = []
i = 0 
for i in range(1400):
	files.append(i)
	
pages = range(1400)
st = 0
for page in pages:
	c = pyautogui.screenshot((str(st) + '.png'))
	st += 1
	pyautogui.press('right')
	pyautogui.PAUSE = 1

