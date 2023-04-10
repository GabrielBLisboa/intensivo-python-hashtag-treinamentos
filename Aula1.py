import pyautogui
import time
import pyperclip

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

with open(r"C:\Users\Gabriel\Desktop\EmpFacul.txt", "r") as f:
    links = f.readlines()
    for x in links:
        link = x.replace("\n", "")
        pyperclip.copy(link)
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        pyautogui.hotkey("ctrl","t")
        time.sleep(1)
