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

        L = ["juan is a hoe \n", "break offff \n", "pussy \n"]
        s = "Hello\n"

        # Writing a string to file
        file1.write(s)

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
        file1 = open('data/data.txt', 'w')
        print("I am unable to see it")
        time.sleep(0.5)
        s = "none"
        file1.write(s)
        file1.close()
