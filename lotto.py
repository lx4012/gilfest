import timeimport pyautoguifrom PIL import Imagefrom PIL import ImageChopsfrom random import randrangedef get_crop(image_resource, start, end):    top = start[0]    left = start[1]    bottom = end[0]    right = end[1]    rectangle = (top, left, bottom, right)    return image_resource.crop(rectangle)def is_contained(a, b):    return not ImageChops.difference(a, b).getbbox()def is_this_element_on_the_screen(element_image_path, element_location_start, element_location_end):    element_image = Image.open(element_image_path)    element_location = get_crop(pyautogui.screenshot(), element_location_start, element_location_end)    return is_contained(element_image, element_location)def wait_until_is_show(element_image_path, element_location_start, element_location_end):    element_image = Image.open(element_image_path)    while True:        time.sleep(1)        element_location = get_crop(pyautogui.screenshot(), element_location_start, element_location_end)        if is_contained(element_image, element_location):            return True    return Falsedef is_box_empty():    point_a = [1549, 354]    point_b = [1724, 391]    return is_this_element_on_the_screen("images/price_reset.bmp", point_a, point_b)def is_present_box_full():    point_a = [1104, 784]    point_b = [1399, 850]    return is_this_element_on_the_screen("images/move_to_present_box_button.bmp", point_a, point_b)def wait_until_prize_is_reset():    point_a = [854, 786]    point_b = [1029, 849]    return wait_until_is_show("images/close_button.bmp", point_a, point_b)# Mainprint("Waiting...")time.sleep(5)print("LETS FUCKING GO")while True:    #press sheba boobs    pyautogui.click(x=620, y=638)    time.sleep(float("0." + str(randrange(4))))    if is_present_box_full():            print("Present Box full")                #press move to present box        pyautogui.click(x=1248, y=819)        break    if is_box_empty():        print("Box empty")        #press reset prize button        pyautogui.click(x=1603, y=368)        time.sleep(1)        #press reset button        pyautogui.click(x=1216, y=825)        wait_until_prize_is_reset()        #press close button        pyautogui.click(x=938, y=822)        time.sleep(1)