import pyscreeze
import PIL
from pynput.mouse import Listener
import numpy as np
import cv2
import pyautogui

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

def click(x,y,button,pressed):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite("image1.png", image)
    print("Mouse is Clicked at (",x,",",y,")","with",button)

with Listener(on_click=click) as listener:
    listener.join()









