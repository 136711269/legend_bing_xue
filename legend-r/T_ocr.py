
from PIL import Image
import pytesseract

# 设置 Tesseract 的路径（如果需要）
# pytesseract.pytesseract.tesseract_cmd = r"E:\Tesseract-OCR\tesseract.exe"  # 根据你的安装路径修改

# 加载图片
image_path = r"C:\Users\admin\Desktop\study_yolo\2321.png" # 替换为你的图片文件路径
image = Image.open(image_path)

# 进行 OCR 识别
text = pytesseract.image_to_string(image, lang='chi_sim')

# 输出识别结果
print(text)
print('请输出结果')
