import pyautogui, time


#get mouse and pixel
while True:
    print('pls input x: ')
    x = input()
    print('pls input y: ')
    y = input()
    # just a trick
    #pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('red.png')))
    if (x == 'q' or y == 'q'):
        break
    pyautogui.moveTo(int(x),int(y),duration=0.5)
    print('now:(',x,',',y,')', 'RGB', pyautogui.screenshot().getpixel((int(x),int(y))))




#pyautogui.click(10,10) # to (10,10) then click
#pyautogui.doubleClick(10,10)
#pyautogui.middleClick(10,10)
#pyautogui.rightClick(10,10)

'''
call paint app to draw sth
time.sleep(5)# 5 senconds to open paint app, quickly move!
distance = 200
while distance>0:
    pyautogui.dragRel(distance,0,duration=0.25)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.25)
    pyautogui.dragRel(-distance, 0, duration=0.25)
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.25)
'''


