import pygetwindow as gw
import win32con
import win32gui
import ctypes
import warnings


def window_always_on_top(window_title):
    warnings.filterwarnings("ignore", ".*64-bit application should be automated using 64-bit Python.*")

    ctypes.windll.kernel32.SetConsoleTitleW(window_title)

    window = gw.getWindowsWithTitle(window_title)[0]

    hwnd = window._hWnd

    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
