import win32api
import win32con
import ImageGrab
import time
from numpy import *


x_pad = 75
y_pad = 23
boolean pressed = false


class Cord:
    accept_match = 482, 406
    text_feild = 267, 665
    play_button = 589, 39


def playGame():
    mousePos((482, 406))
    leftClick()
    time.sleep(.1)
    return


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print ("Click.")


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1151, y_pad + 719)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
    #'.png', 'PNG')
    textFeildColor = im.getpixel((300, 663))
    print (textFeildColor)
    return im


def clickAndType():
    print("hi I am clicked and typed")
    s = screenGrab()
    if s.getpixel != (2, 8, 15):
        print("I am in the if")
        mousePos((267, 665))
        leftClick()
        pressed = true


playGame()
while (!pressed):
    clickAndType()


#def main():
    #playGame()
    #screenGrab()




