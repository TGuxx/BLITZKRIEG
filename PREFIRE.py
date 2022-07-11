import time
import pyautogui as p

WITHDRAW_COLOR = (0,199,77)
WITHDRAW_REGION = (744,321,1,1)
WITHDRAW_BTN = (0,0)

def SolveCaptcha():
    start_time = time.time()
    seconds = 3

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        p.click(300,473)

        if elapsed_time > seconds:
            p.click()
            break 
    main()

def main():
    while True:
        p.click(120,710)
        
        im = p.screenshot(region=WITHDRAW_REGION)
        
        withdraw_pos = im.getpixel(WITHDRAW_BTN)
        
        if withdraw_pos == WITHDRAW_COLOR:
            p.click(742,348)
            SolveCaptcha()
            
print("Running PREFIRE [1024x768]...")
main()
