import pyautogui, time, schedule
from cordinates import chrome_close


pyautogui.PAUSE = 2
# pyautogui.hotkey('win','d')
time.sleep(2)

claim_daily = r"C:\Users\amit9\Desktop\autopygui\Work Temp\img\soquest.png"
refress = r"C:\Users\amit9\Desktop\autopygui\img\chrome_refress.png"
pass_png = r"C:\Users\amit9\Desktop\autopygui\img\meta pass img.png"
meta_down_icon = r"C:\Users\amit9\Desktop\autopygui\img\meta_down_icon.png"
meta_sign = r"C:\Users\amit9\Desktop\autopygui\img\meta_sign.png"

def claim():
    no = 5
    for i in range(4):

        if no<9:

            pyautogui.hotkey('win','r')
            pyautogui.typewrite("chrome"+str(no)); pyautogui.press('enter')

            #code
            while True:
                result = pyautogui.locateOnScreen(refress, confidence=0.8)
                if refress is not None:
                    pyautogui.hotkey('alt','shift','m')
                    time.sleep(5)
                break

            while True:
                result = pyautogui.locateOnScreen(meta_down_icon, confidence=0.8, region=[1135,83,1651,168])
                if result is not None:
                    if (pyautogui.locateAllOnScreen(pass_png, confidence=0.6) is not None):
                        pyautogui.typewrite("Ankit9517"); pyautogui.press("enter"); pyautogui.sleep(5)
                        pyautogui.click(334,64)
                        break
                    else:
                        pyautogui.click(334,64)
                        break
                break
                    
            
            pyautogui.typewrite("https://soquest.xyz/privilege"); pyautogui.press('enter'); time.sleep(3)
            while True:
                if (pyautogui.locateCenterOnScreen(meta_sign, confidence=0.6) is not None):
                    x, y = pyautogui.locateCenterOnScreen(meta_sign, confidence=0.6)
                    time.sleep(2); pyautogui.click(x, y)
                    break
            
            while True:
                if (pyautogui.locateOnScreen(claim_daily, confidence=0.6)is not None):
                    pyautogui.click(claim_daily)
                    break
            
            pyautogui.click(chrome_close)
            print("chrome",no,"Done")
            no = (no++1)

        else:
            print("g")

# schedule.every().day.at("10:10").do(claim)
claim()
while 1:
    schedule.run_pending()
    time.sleep(3)
exit
