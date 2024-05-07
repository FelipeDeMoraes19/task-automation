import time
import pyautogui
import pandas as pd

pyautogui.PAUSE = 0.3

def abrir_navegador(url):
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(5) 
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(3) 



