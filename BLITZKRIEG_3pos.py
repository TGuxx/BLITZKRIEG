import time
import pyautogui as p

#COLORS (USE OWN VALUES)
BLITZ_COLOR = (0,226,88)
WITHDRAW_COLOR = (0,199,77)

#SCREENSHOT REGIONS (FULLHD)
BLITZ_REGION = (454,653,385,3)
WITHDRAW_REGION = (1800,320,1,1)

#BLITZ 
B1_POS=(5,1)
B2_POS=(190,1)
B3_POS=(375,1)

VOID = (300,300)

#WITHDRAW
WITHDRAW_BTN = (0,0)

def SolveCaptcha():
    start_time = time.time()
    seconds = 3

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        p.click(750,620)

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
            p.click(1638,350)
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
            p.click(460, 612)
            StartWithdraw()

        b_pos2 = im.getpixel(B2_POS)
        if b_pos2 == BLITZ_COLOR:
            p.click(645, 612)
            StartWithdraw()

        b_pos3 = im.getpixel(B3_POS)
        if b_pos3 == BLITZ_COLOR:
            p.click(830, 612)
            StartWithdraw()
            
        p.click(VOID)  

print("Running BLITZKRIEG 3 POS...")
main()
