import win32api
import win32con
import win32gui
import time

def leftClick(hwnd, pos):
    lParam = win32api.MAKELONG(pos[0], pos[1])

    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam) 
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)
    time.sleep(0.1)


hwnd = win32gui.FindWindow(None, "녹스 플레이어")

leftClick(hwnd, [200,200])