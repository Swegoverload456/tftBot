from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    #SIZE OF SHOP PICS IS 85 x 14 pixels unless gold
    #GOLD NEEDS A DIFFERENT DETECTION SYSTEM
    #GOLD IS 26 x 10 pixels and 4 pixels away from bright yellow line on the left
    #JUST DO A CONFIDENCE RATING ON THE GOLDS
    if pyautogui.locateOnScreen('shopImages/') is not None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)





    if pyautogui.locateOnScreen('shopImages/Teemo.png', region = (560, 950, 87, 14), confidence=0.8) is not None:
        file1 = open('data/data.txt', 'w')
        print("I can see it")
        list = ["none\n", "none\n", "none\n", "none\n", "none\n"]
        list[0]="fiora\n"
        L = [list[0],list[1],list[2],list[3],list[4]]

        # Writing multiple strings
        # at a time
        file1.writelines(L)

        # Closing file
        file1.close()

        # Checking if the data is
        # written to file or not
        file1 = open('data/data.txt', 'r')
        print(file1.read())
        file1.close()
        time.sleep(3)
    else:
        list = ["none\n", "none\n", "none\n", "none\n", "none\n"]
        list[0] = "fiora\n"
        L = [list[0],list[1],list[2],list[3],list[4]]
        file1 = open('data/data.txt', 'w')
        print("I am unable to see it")
        time.sleep(3)
        file1.writelines(L)
        file1.close()