import time
import math
import pyautogui
import cv2
import numpy as np

def find_image_on_screen(target_image_path, confidence=0.90, region=(0, 0, 1031, 800)):
    # 读取目标图像和屏幕截图
    target_image = cv2.imdecode(np.fromfile(target_image_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot(region=region)

    # 将屏幕截图转换为灰度图像
    screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)

    # 使用 OpenCV 的模板匹配方法进行图像匹配
    res = cv2.matchTemplate(screen_gray, target_image, cv2.TM_CCOEFF_NORMED)
    # 获取匹配结果的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= confidence:
        # 找到了目标图像，返回位置
        target_center = (max_loc[0] + target_image.shape[1] // 2, max_loc[1] + target_image.shape[0] // 2)
        return target_center
        # return True
    else:
        # 未找到目标图像
        return False


def find_all_images_on_screen(target_image_path, confidence=0.90, region=(0, 0, 1020, 550)):
    # 读取目标图像和屏幕截图
    target_image = cv2.imdecode(np.fromfile(target_image_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    screen = pyautogui.screenshot(region=region)

    # 将屏幕截图转换为灰度图像
    screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)

    # 使用 OpenCV 的模板匹配方法进行图像匹配
    res = cv2.matchTemplate(screen_gray, target_image, cv2.TM_CCOEFF_NORMED)

    # 设定一个匹配结果的阈值
    threshold = confidence
    loc = np.where(res >= threshold)

    # 初始化一个列表来存储所有匹配到的目标中心位置
    target_centers = []

    for pt in zip(*loc[::-1]):
        # 计算每个匹配到的目标的中心位置
        target_center = (pt[0] + target_image.shape[1] // 2, pt[1] + target_image.shape[0] // 2)
        target_centers.append(target_center)

        # 返回所有匹配到的目标中心位置列表
    return target_centers



# 计算两点之间的欧几里得距离
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# 筛选出距离目标点200像素以上的坐标
def filter_far_coordinates(coordinates, reference_point, distance_threshold=200):
    far_coords = [coord for coord in coordinates if calculate_distance(coord, reference_point) > distance_threshold]
    return far_coords

# 计算200像素以内的坐标数量
def count_close_coordinates(coordinates, reference_point, distance_threshold=200):
    close_coords = [coord for coord in coordinates if calculate_distance(coord, reference_point) <= distance_threshold]
    return len(close_coords), close_coords

# 查找屏幕上所有匹配的目标图像，并筛选和处理
def find_and_process_targets(target_image_path='img/怪物.png', reference_point=(533, 309), confidence=0.95, region=(0, 0, 1020, 550)):
    # 调用find_all_images_on_screen获取所有匹配目标的坐标
    target_centers = find_all_images_on_screen(target_image_path, confidence, region)

    # 筛选出距离参考点(533, 309) 200像素以上的坐标
    far_coordinates = filter_far_coordinates(target_centers, reference_point)

    # 计算距离参考点200像素以内的数量
    close_count, close_coordinates = count_close_coordinates(target_centers, reference_point)

    if close_count > 8:
        print("周围怪物很多")
    else:
        if far_coordinates:
            # 查找距离最远的坐标
            farthest_coord = max(far_coordinates, key=lambda coord: calculate_distance(coord, reference_point))
            print(f"点击距离最远的怪物: {farthest_coord}")
            # 模拟点击操作
            # re_number.move_to_target((farthest_coord[0], farthest_coord[1] + 46))
            # pyautogui.click(farthest_coord[0], farthest_coord[1] + 46)
#
#
#
    return far_coordinates, close_coordinates


def find_red_color():
    # 获取屏幕截图
    screenshot = pyautogui.screenshot(region=(861, 31, 173, 158))
    screenshot_np = np.array(screenshot)

    # 转换颜色空间，从RGB到BGR
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # 定义红色的范围
    lower_red = np.array([0, 0, 255])  # BGR
    upper_red = np.array([100, 100, 255])  # 可能的红色范围

    # 创建掩码
    mask = cv2.inRange(screenshot_bgr, lower_red, upper_red)

    # 找到红色区域的轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    red_coordinates = []

    if red_coordinates:
        print('发现怪物')
    else:
        print('没有发现怪物')

    for contour in contours:
        # 计算轮廓的边界框
        x, y, w, h = cv2.boundingRect(contour)
        red_coordinates.append((x + w // 2, y + h // 2))  # 记录中心点

    return red_coordinates




def is_monster():
    monster_path = 'img/monster'


if __name__ == '__main__':
    time.sleep(1)
    # res =find_image_on_screen('img/高级传送/神魔秘境-秘境使者.png')

    res = find_red_color()
    print(res)
    if res:
        for i in range(len(res)):
            print(res[i][0] + 861, res[i][1] + 31)


