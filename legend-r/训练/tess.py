import pytesseract

from PIL  import Image
import cv2
import numpy as np
import mss
import pyautogui
from PIL.ImageChops import screen


region = (60, 781, 60, 20)
screenshot = pyautogui.screenshot(region=region)
screenshot.save('test.png')
custom_config = r'--oem 3 --psm 6 outputbase digits '
text = pytesseract.image_to_string(screenshot, config=custom_config)
print(text)

def preprocess_image(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    return gray

def capture_screen_and_ocr():
    with mss.mss() as sct:
        monitor = {"top": 60, "left":781, "width": 60, "height": 20}
        img = sct.grab(monitor)

        img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
        img = preprocess_image(img)
        text = pytesseract.image_to_string(img)
        print(text)


# capture_screen_and_ocr()