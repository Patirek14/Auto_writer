import pyautogui
import time
import random

msg = input("Wpisz wiadomosc: ")
n = input("ile razy ?: ")

print("t minus")

count = 3
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print()

for i in range(0,int(n)):
    for c in msg:
            pyautogui.typewrite(c)
            rand = random.randrange(0,100)
            rand /= 500
            time.sleep(rand)
    pyautogui.typewrite('\n')
