from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:


    if pyautogui.locateOnScreen('shopImages/Jhin.PNG') is not None:
        file1 = open('data/data.txt', 'w')
        print("I can see it")
        list = ["none\n", "none\n", "none\n", "none\n", "none\n"]
        list[0]="jhin\n"
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
        time.sleep(0.5)
    else:
        list = ["none\n", "none\n", "none\n", "none\n", "none\n"]
        list[0] = "jhin\n"
        L = [list[0],list[1],list[2],list[3],list[4]]
        file1 = open('data/data.txt', 'w')
        print("I am unable to see it")
        time.sleep(0.5)
        file1.writelines(L)
        file1.close()
