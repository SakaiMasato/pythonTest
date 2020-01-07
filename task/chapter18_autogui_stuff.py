import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width, height = pyautogui.size()
for i in range(0, 500, 50):
    print(pyautogui.position())
    pyautogui.moveTo(i + 50, i + 50, duration=1)
    pyautogui.moveTo(i + 100, i + 100, duration=1)
    pyautogui.moveTo(i + 150, i + 150, duration=1)
    pyautogui.moveTo(i + 200, i + 200, duration=1)