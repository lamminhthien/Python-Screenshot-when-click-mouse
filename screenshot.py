import pyscreeze
import PIL
from pynput.mouse import Listener
import numpy as np
import cv2
import pyautogui

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

imageName=input("Please enter name for picture: ")
quantity = 0

def takeScreenshot(x,y,button,pressed):
    if pressed:
        imageRaw = pyautogui.screenshot()
        imageRaw = cv2.cvtColor(np.array(imageRaw),cv2.COLOR_RGB2BGR)
        global quantity
        quantity = quantity + 1
        imageFileName = imageName + str(quantity) + ".png"
        cv2.imwrite(imageFileName, imageRaw)
        print("Captured image:" + imageFileName)

with Listener(on_click=takeScreenshot) as listener:
    listener.join()











