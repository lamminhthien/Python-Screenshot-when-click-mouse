import pyscreeze
import PIL
from pynput.mouse import Listener
import numpy as np
import cv2
import pyautogui

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

imageName=input("Please enter name for picture: ")
count = 0


def click(x,y,button,pressed):
    if pressed:
        imageRaw = pyautogui.screenshot()
        imageRaw = cv2.cvtColor(np.array(imageRaw),cv2.COLOR_RGB2BGR)
        global count
        count = count + 1
        cv2.imwrite(imageName + str(count) + ".png", imageRaw)
        print("Mouse is Clicked at (",x,",",y,")","with",button)

with Listener(on_click=click) as listener:
    listener.join()











