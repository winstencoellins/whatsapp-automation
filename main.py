import pywhatkit
import pyautogui as pg
import time
import pandas as pd

# df = pd.read_excel("./data/recipient.xlsx")

# recipient = df['Nomor Telepon'].to_numpy()

# for i in recipient:
#     print(i)

# als;fja;lkdsj;lajdflja;jj

test = ["+6287829112648", "+628116359119"]

msg = "Anda diundang untuk menghadiri acara graduation MSJ GMS."

try:
    for i in test:
        pywhatkit.sendwhatmsg_instantly(i, msg, 15, True, 5)

        time.sleep(1)
        pg.leftClick()

        pg.press("enter")
except:
    print("Internet connection error.")