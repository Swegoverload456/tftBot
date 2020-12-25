from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#coords for shop
#champ slot 1: x = 561, y = 951, w = 86, h = 14
#champ slot 2: x = 728, y = 951, w = 86, h = 14
#champ slot 3: x = 896, y = 951, w = 86, h = 14
#champ slot 4: x = 1064, y = 951, w = 86, h = 14
#champ slot 5: x = 1232, y = 951, w = 86, h = 14
time.sleep(0.75)
location = pyautogui.locateOnScreen('shopImages/Lulu.png', region=(561, 951, 86, 14), confidence=0.7)
print(location)
