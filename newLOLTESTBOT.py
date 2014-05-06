import win32api
import win32con
import ImageGrab
import time
from numpy import *



x_pad = 75
y_pad = 23






def playGame():
    mousePos((589, 39))
    leftClick()
    time.sleep(.1)
    print ("HI")
    return;


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print "Click."

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


playGame();