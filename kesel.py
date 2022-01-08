import pyautogui as auto
import time

message = "Buka Blokiran"
n = 200

time.sleep(2)

for i in range(n):
    auto.typewrite(message + '\n')