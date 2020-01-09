import pyautogui,time

time.sleep(5)
point = pyautogui.Point(1000,750)
pyautogui.moveTo(point, duration=0.25)
while True:
    time.sleep(3*60)
    pyautogui.click(1000,750)
