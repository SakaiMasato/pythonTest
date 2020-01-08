import pyautogui,time

while True:
    time.sleep(5*60)
    nowPosition = pyautogui.position()
    print(nowPosition)
    x,y = nowPosition.x, nowPosition.y
    newPosition = pyautogui.Point(x+1,y+1)
    pyautogui.moveTo(newPosition,duration=0.25)
