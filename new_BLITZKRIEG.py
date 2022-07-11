import time
import pyautogui as p

#COLORS (USE OWN VALUES)
BLITZ_COLOR = (0,226,88)
WITHDRAW_COLOR = (0,199,77)

#SCREENSHOT REGIONS (FULLHD)
BLITZ_REGION = (208,762,469,2)
WITHDRAW_REGION = (744,321,1,1)

#BLITZ 
B1_POS=(6,0)
B2_POS=(235,0)
B3_POS=(463,0)

VOID = (32,316)

#WITHDRAW
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

def StartWithdraw():
    start_time = time.time()
    seconds = 2

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # SCREENSHOT
        im = p.screenshot(region=WITHDRAW_REGION)
        
        # CHECKING PHASE
        withdraw_pos = im.getpixel(WITHDRAW_BTN)
        if withdraw_pos == WITHDRAW_COLOR:
            p.click(742,348)
            break

        if elapsed_time > seconds:
            main()
    SolveCaptcha()

def main():
    while True:
        # SCREENSHOT
        im = p.screenshot(region=BLITZ_REGION)

        # CHECKING PHASE
        b_pos1 = im.getpixel(B1_POS)
        if b_pos1 == BLITZ_COLOR:
            p.click(120,710)
            StartWithdraw()

        b_pos2 = im.getpixel(B2_POS)
        if b_pos2 == BLITZ_COLOR:
            p.click(340,700)
            StartWithdraw()

        b_pos3 = im.getpixel(B3_POS)
        if b_pos3 == BLITZ_COLOR:
            p.click(580,710)
            StartWithdraw()
        p.click(VOID)  

print("Running NEW BLITZ 3 POS...")
main()
