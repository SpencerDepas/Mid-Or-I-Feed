from Tkinter import *
import win32api
import win32con
import time
from numpy import *
import win32com.client

master = Tk()
shell = win32com.client.Dispatch("WScript.Shell")
x_pad = 75
y_pad = 23


e = Entry(master)
e.pack()

e.focus_set()


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def playGame():
    mousePos((482, 406))
    leftClick()
    time.sleep(.1)
    return


def midOrIfeed(str):
    mousePos((300, 663))
    leftClick()
    #time.sleep(.1)
    #shell.SendKeys("Mid Or I Feed")
    shell.SendKeys(str)
    shell.SendKeys("{ENTER}")
    time.sleep(3)
    return


def callback():
    position = e.get()
    playGame()
    currentTime = time.time()
    while(currentTime + 8 > time.time()):
        midOrIfeed(position)


b = Button(master, text="Position", width=10, command=callback)
b.pack()

mainloop()