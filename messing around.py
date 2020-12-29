import os
import pyautogui
import numpy as np
import cv2 as cv
from time import time
from PIL import  ImageGrab


os.chdir(os.path.dirname(os.path.abspath(__file__)))

loop_time = time()
while(True):
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot= cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow ('Computer vision',screenshot)
    print('FPS {}'.format(1/(time()- loop_time)))
    loop_time = time()

    if cv.waitKey(1)== ord('q'):
        cv.destroyAllWindows()
        break
print("done")