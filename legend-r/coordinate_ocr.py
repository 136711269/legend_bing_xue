import pytesseract
from PIL import Image
import cv2

# 读取图像并进行灰度处理
img = cv2.imread(r"C:\Users\admin\Desktop\test_1.png", cv2.IMREAD_GRAYSCALE)

# 尝试不同的二值化阈值来提高文本可见度
_, img_thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

# 可选：对图像进行放大，提高分辨率
img_resized = cv2.resize(img_thresh, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# 转换为 PIL 图像
pil_img = Image.fromarray(img_resized)

# 定义 Tesseract 配置，指定只识别数字和中文字符
custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789./盟重省'

# 使用 Tesseract 进行文字识别
res = pytesseract.image_to_string(pil_img, lang='chi_sim', config=custom_config)

print(res)