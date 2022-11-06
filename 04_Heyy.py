
import pyautogui
import time
time.sleep(5)

# a = input("Enter any thing you want to show your user:\n")
# b = int(input("Enter any number:\n"))
count=0

while count<=100:
    pyautogui.typewrite("I hate you")
    pyautogui.press("enter")
    count=count+1




