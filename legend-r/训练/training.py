import pytesseract
from PIL import Image

# 读取图片
image = Image.open(r"C:\Users\admin\Desktop\test_1.png")



# 进行 OCR 识别
text = pytesseract.image_to_string(image)
print(text)