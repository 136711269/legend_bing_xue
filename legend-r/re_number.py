import cv2
import numpy as np
import pyautogui
import opration
import win32con, win32gui, time, math
import threading
import Find_Pic
def match_template(image, template, threshold=0.9):
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    return zip(*loc[::-1])  # 返回坐标 (x, y)

def recognize_coordinates(image_path, templates):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    recognized_text = ""
    matches_info = []

    # 遍历模板列表（0-9 和冒号）
    for label, template in templates.items():
        matches = match_template(image, template)
        for pt in matches:
            matches_info.append((pt[0], label))

    matches_info.sort(key=lambda x: x[0])
    recognized_text = "".join(label for _, label in matches_info)

    return recognized_text

def load_templates(template_dir):
    templates = {}
    for num in range(10):
        template_path = f"{template_dir}/number{num}.png"
        templates[str(num)] = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    templates[":"] = cv2.imread(f"{template_dir}/maohao.png", cv2.IMREAD_GRAYSCALE)

    return templates

def get_current_coordinate(region=(45, 778, 135, 20)):
    template_dir = 'number/'
    templates = load_templates(template_dir)

    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('coord.png')
    image_path = 'coord.png'

    recognized_text = recognize_coordinates(image_path, templates)
    print("当前人物的坐标：", recognized_text)

    if recognized_text:
        x, y = recognized_text.split(':')
        return int(x), int(y)
    else:
        return None, None



"""以下函数为移动到目的地坐标"""



# 根据当前坐标和目标坐标，判断是否到达目标
def reached_target(current_coord, target_coord, threshold=2):
    # 判断是否在目标坐标附近，允许一个误差范围 threshold
    return abs(current_coord[0] - target_coord[0]) <= threshold and abs(current_coord[1] - target_coord[1]) <= threshold


# 根据当前坐标和目标坐标，计算移动的方向
def calculate_direction(current_coord, target_coord):
    delta_x = target_coord[0] - current_coord[0]
    delta_y = target_coord[1] - current_coord[1]

    # Normalize the direction vector (dx, dy) to one of 8 directions

    angle = math.atan2(delta_y, delta_x) * 180 / math.pi  # Convert to degrees
    if -22.5 <= angle < 22.5:
        return 'right'
    elif 22.5 <= angle < 67.5:
        return 'down_right'
    elif 67.5 <= angle < 112.5:
        return 'down'
    elif 112.5 <= angle < 157.5:
        return 'down_left'
    elif 157.5 <= angle or angle < -157.5:
        return 'left'
    elif -157.5 <= angle < -112.5:

        return 'up_left'
    elif -112.5 <= angle < -67.5:
        return 'up'
    elif -67.5 <= angle < -22.5:
        return 'up_right'


target_coordinates = {
    'up': (544, 182),
    'down': (538, 495),
    'left': (350, 310),
    'right': (769, 303),
    'up_left': (382, 159),
    'up_right': (691, 173),
    'down_left': (388, 467),
    'down_right': (711, 435)
}


#
# def move_to_target( target_coord, region=(45, 778, 140, 20)):
#
#     try:
#         start_time = time.time()
#         while True:
#             end_time = time.time()
#             if end_time - start_time > 100:
#                 break
#             time.sleep(0.1)
#             # 获取当前坐标
#             current_coord = get_current_coordinate(region)
#
#
#
#             # 计算方向
#             direction = calculate_direction(current_coord, target_coord)
#             opration.move_mouse(target_coordinates[direction][0], target_coordinates[direction][1])
#
#             opration.send_right_mouse_down(target_coordinates[direction][0], target_coordinates[direction][1])
#
#             if reached_target(current_coord, target_coord):
#                 print(f"到达目标坐标: {target_coord}")
#                 opration.send_right_mouse_up(target_coordinates[direction][0], target_coordinates[direction][1])
#
#                 break  # 目标到达时停止移动
#
#
#             time.sleep(0.05)  # 等待一小段时间后再次检测坐标
#     finally:
#         pass


def move_to_target(target_coord, region=(45, 778, 140, 20)):

    start_time = time.time()
    while True:
        end_time = time.time()

        time.sleep(0.5)
        # 获取当前坐标
        current_coord = get_current_coordinate(region=region)

        # 计算方向
        direction = calculate_direction(current_coord, target_coord)
        opration.move_mouse(target_coordinates[direction][0], target_coordinates[direction][1])

        opration.send_right_mouse_down(target_coordinates[direction][0], target_coordinates[direction][1])

        if reached_target(current_coord, target_coord):
            print(f"到达目标坐标: {target_coord}")
            opration.send_right_mouse_up(target_coordinates[direction][0], target_coordinates[direction][1])
            break  # 目标到达时停止移动
        if end_time - start_time > 60:
            opration.send_right_mouse_up(target_coordinates[direction][0], target_coordinates[direction][1])
            opration.go_home()
            break
        s_h_tag = Find_Pic.find_image_on_screen('img/首饰店.png')
        if s_h_tag:
            opration.send_right_mouse_up(target_coordinates[direction][0], target_coordinates[direction][1])
            opration.go_home()
            break
        time.sleep(0.05)  # 等待一小段时间后再次检测坐标




# 示例调用
# start_coord = (1312, 287)
# target_coord = (538, 457)
# region = None  # 自定义坐标区域
# move_to_target(start_coord, target_coord, region)

# 示例使用
if __name__ == "__main__":
    # 获取窗口句柄
    window_handle = win32gui.FindWindow(None, '热血华山15区(16:00)')
    # 移动窗口到0，0位置
    win32gui.SetWindowPos(window_handle, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)
    # 激活窗口
    opration.activate_game_window()
    # # 激活
    # time.sleep(1)
    # pyautogui.click(3, 3)
    region = (45, 778, 100, 20)  # 根据需要调整截取区域
    # current_coordinate = get_current_coordinate(region)
    destination_coordinate = (333, 339)  # Example target
    move_to_target( destination_coordinate, region)

