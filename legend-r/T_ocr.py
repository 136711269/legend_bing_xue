import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np

from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

# 初始化 PaddleOCR，设置语言为中文
ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # lang='ch' 表示中文

# 读取图片路径
img_path = 'ditu.png'

# 进行 OCR 识别
result = ocr.ocr(img_path, cls=True)
print(result)

# 打印识别结果
# for line in result[0]:
#     print("识别的文字：", line[1][0])
#     print("置信度：", line[1][1])
#
# # 可选：在图像上绘制识别结果
# # 打开图片
# image = Image.open(img_path).convert('RGB')
# boxes = [elements[0] for elements in result[0]]  # 获取文本区域的坐标
# txts = [elements[1][0] for elements in result[0]]  # 获取识别的文字
# scores = [elements[1][1] for elements in result[0]]  # 获取置信度
#
# # 绘制 OCR 结果
# im_show = draw_ocr(image, boxes, txts, scores, font_path=r"D:\ProgramFiles\996box\GameBoxDownload\1\cq\mod_launcher\stab\fonts\font.ttf")
# im_show = Image.fromarray(im_show)
# im_show.show()  # 显示图片