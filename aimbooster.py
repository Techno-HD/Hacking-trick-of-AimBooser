from pyautogui import *
import pyautogui as gui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
	pic=gui.screenshot(region=(306,229,747,431))
	w,h=pic.size
	for i in range(0,w,5):
		for j in range(0,h,5):
			r,g,b=pic.getpixel((i,j))
			if b in range(30,40):
				click(i+306,j+229)
				time.sleep(0.05)
				break