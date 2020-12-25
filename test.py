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
    if pyautogui.locateOnScreen('shopImages/Jhin.PNG') is not None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
