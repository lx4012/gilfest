import cv2
import time
import numpy as np
import pyautogui

def is_in_range(a, b):
    _min = a - 25
    _max = a + 25

    return b > _min and b < _max

exp_silver = cv2.imread('images/exp.bmp', 0)
exp_x1 = cv2.imread('images/X1.bmp', 0)
exp_x2 = cv2.imread('images/X2.bmp', 0)

def select_this_item(template, img_rgb, distance):

    threshold = 0.8
    sabrosura = -999

    w, h = template.shape[::-1]
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)

    count = 0

    for pt in zip(*loc[::-1]):

        if not is_in_range(sabrosura, pt[1] + h):

            if sabrosura == -1:
                time.sleep(0.5)

            sabrosura = pt[1] + h
            pyautogui.click(x=1230, y=(sabrosura + distance))
            print("YEET")
            time.sleep(0.5)
            count += 1
    return count

loot_count = 0

loot_silver = True
loot_x1 = False
loot_x2 = False

print("Waiting...")
time.sleep(5)
print("LETS FUCKING GO")

while True:

    current_screen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR)

    # select desired items
    if loot_silver:
        loot_count = loot_count + select_this_item(exp_silver, current_screen, 18)
    else:
        if loot_x1:
            loot_count = loot_count + (2*select_this_item(exp_x1, current_screen, 25))
        if loot_x2:
            loot_count = loot_count + (2*select_this_item(exp_x2, current_screen, 25))

    if loot_count > 98:
        print("Max loot reached")
        break

    # scroll down
    pyautogui.moveTo(707, 883)
    time.sleep(0.5)
    pyautogui.dragTo(707, 124, 3)
    time.sleep(0.5)