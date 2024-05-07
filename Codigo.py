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

def fazer_login(email, senha):
    pyautogui.click(x=685, y=451) 
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    time.sleep(1) 
    pyautogui.click(x=955, y=660)
    time.sleep(3)


