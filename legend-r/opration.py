import time



import re_number
import pyautogui
import win32gui
import win32api
import win32con
import Find_Pic
import pygetwindow as gw
coordinate = {'img/小秘书': (35, 339), 'img/高级传送':(230, 292), 'img/起源冰城':(391, 248), 'img/自动挂机':(990, 376)}

active_window = None
default_title = "热血华山15区(16:00)"

def activate_game_window(window_title=default_title):
    global active_window
    try:
        # 查找窗口
        active_window = gw.getWindowsWithTitle(window_title)[0]
        print(f"已激活窗口: {window_title}")
    except IndexError:
        print("窗口未找到！请确认窗口标题。")
        active_window = None


def send_left_click(x_offset, y_offset, window=None):
    """发送左键点击消息"""
    if window is None:
        window = active_window
    if window is not None:
        x = window.left + x_offset
        y = window.top + y_offset
        hwnd = window._hWnd

        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, (y << 16) | x)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, (y << 16) | x)
        print(f"已在({x}, {y})位置左键点击。")
    else:
        print("请先激活窗口。")


def send_right_click(x_offset, y_offset, window=None):
    """发送右键点击消息"""
    if window is None:
        window = active_window
    if window is not None:
        x = window.left + x_offset
        y = window.top + y_offset
        hwnd = window._hWnd

        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, (y << 16) | x)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, 0, (y << 16) | x)
        print(f"已在({x}, {y})位置右键点击。")
    else:
        print("请先激活窗口。")


def send_mouse_down(x_offset, y_offset, window=None):
    """发送鼠标按下消息（左键）"""
    if window is None:
        window = active_window
    if window is not None:
        x = window.left + x_offset
        y = window.top + y_offset
        hwnd = window._hWnd

        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, (y << 16) | x)
        print(f"已在({x}, {y})位置左键按下。")
    else:
        print("请先激活窗口。")


def send_mouse_up(x_offset, y_offset, window=None):
    """发送鼠标弹起消息（左键）"""
    if window is None:
        window = active_window
    if window is not None:
        x = window.left + x_offset
        y = window.top + y_offset
        hwnd = window._hWnd

        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, (y << 16) | x)
        print(f"已在({x}, {y})位置左键弹起。")
    else:
        print("请先激活窗口。")


def send_right_mouse_down(x_offset, y_offset, window=None):
    """发送鼠标右键按下消息"""
    if window is None:
        window = active_window
    if window is not None:
        x = window.left + x_offset
        y = window.top + y_offset
        hwnd = window._hWnd

        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, (y << 16) | x)
        print(f"已在({x}, {y})位置右键按下。")
    else:
        print("请先激活窗口。")


def send_right_mouse_up(x_offset, y_offset, window=None):
    """发送鼠标右键弹起消息"""
    if window is None:
        window = active_window
    if window is not None:
        x = window.left + x_offset
        y = window.top + y_offset
        hwnd = window._hWnd

        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, 0, (y << 16) | x)
        print(f"已在({x}, {y})位置右键弹起。")
    else:
        print("请先激活窗口。")


def move_mouse(x_offset, y_offset, window=None):
    """移动鼠标到指定位置"""
    if window is None:
        window = active_window
    if window is not None:
        x = window.left + x_offset
        y = window.top + y_offset
        win32api.SetCursorPos((x, y))
        print(f"鼠标移动到({x}, {y})位置。")
    else:
        print("请先激活窗口。")

def click(x, y):
    time.sleep(1)
    send_left_click(x, y)
    # pyautogui.click(x, y)
    # time.sleep(0.5)
    # pyautogui.click(x, y)

def click_monster(x, y):
    # pyautogui.moveTo(x, y)
    move_mouse(x,y)
    send_left_click(x, y)
    # pyautogui.leftClick()

def click_right(x, y):
    time.sleep(1)
    send_right_click(x, y)
    # pyautogui.rightClick(x, y)
    # pyautogui.leftClick()


def move_click(x, y):
    time.sleep(0.5)
    # pyautogui.moveTo(x, y, duration=0.1)
    move_mouse(x, y)
    time.sleep(0.5)
    # pyautogui.leftClick()
    send_left_click(x, y)

def move_click_right(x, y):
    time.sleep(1)
    # pyautogui.moveTo(x, y, duration=0.1)
    move_mouse(x, y)
    # print(f'鼠标移动到{x,y}')
    time.sleep(0.5)
    # pyautogui.rightClick()
    send_right_click(x, y)


def move_pic_click_right(pic_path):
    time.sleep(1)
    target = Find_Pic.find_image_on_screen(pic_path)
    if target:
        print(pic_path)
        move_click_right(target[0], target[1])
    else:
        print(f'点击失败{pic_path}')

def move_pic_click_left(pic_path):
    time.sleep(1)
    target = Find_Pic.find_image_on_screen(pic_path)
    if target:
        print(pic_path)
        move_click(target[0], target[1])
    else:
        print(f'点击失败{pic_path}')

def go_home():
    time.sleep(0.5)
    mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    if not mengchong_tag:
        move_pic_click_right('img/回城石.png')

def use_random():
    time.sleep(0.5)
    suiji_tag = Find_Pic.find_image_on_screen('img/随机石.png', confidence=0.7)
    if suiji_tag:
        move_click_right(suiji_tag[0], suiji_tag[1])
        # move_pic_click_right('img/随机石.png')




def buy_random():
    move_pic_click('img/商城.png')
    move_pic_click('img/商城-随机.png')
    move_pic_click('img/商城加号.png')
    move_pic_click('img/商城购买.png')


def read_number(number_path):
    with open(number_path, 'r') as f:
        number = f.read()
    return int(number)

def write_number(number_path, number):
    with open(number_path, 'w') as f:
        f.write(str(number))



def move_pic_click(pic_path, region=(0, 0, 1031, 800),confidence=0.85):
    i = 0
    while i < 10:
        time.sleep(0.5)
        pic_tag = Find_Pic.find_image_on_screen(pic_path, region=region, confidence=confidence)
        if pic_tag:
            print(pic_path)
            move_click(pic_tag[0], pic_tag[1])
            time.sleep(0.5)
            break
        else:
            print(f'点击失败{pic_path}')
        i += 1

def move_pic_click_jia(pic_path, region=(0, 0, 1031, 800), confidence=0.9):
    i = 0
    while i < 10:
        time.sleep(0.5)
        pic_tag = Find_Pic.find_image_on_screen(pic_path, region=region, confidence=confidence)
        if pic_tag:
            print(pic_path)
            move_click(pic_tag[0] + region[0], pic_tag[1]+region[1])
            time.sleep(0.5)
            break
        else:
            print(f'点击失败{pic_path}')
        i += 1

def move_up_left(sec):
    time.sleep(0.5)
    # pyautogui.moveTo(408, 222)
    move_mouse(408,222)
    send_mouse_down(408, 222)
    # pyautogui.mouseDown()
    time.sleep(sec)
    send_mouse_up(408, 222)
    # pyautogui.mouseUp()

def move_up(sec):
    time.sleep(0.5)
    # pyautogui.moveTo(558, 188)
    move_mouse(558,188)
    pyautogui.mouseDown()
    send_mouse_down(558, 188)
    time.sleep(sec)
    # pyautogui.mouseUp()
    send_mouse_up(558, 188)

def move_down(sec):
    time.sleep(0.5)
    move_mouse(558, 427)
    send_mouse_down(558, 427)
    # pyautogui.moveTo(558, 427)
    # pyautogui.mouseDown()
    time.sleep(sec)
    send_mouse_up(558, 427)
    # pyautogui.mouseUp()

def click_zidong():
    mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    if not mengchong_tag:
        zidong_tag = Find_Pic.find_image_on_screen('img/自动挂机.png')
        if zidong_tag:
            move_click(zidong_tag[0], zidong_tag[1])



def guan_bi():
    guan_bi_tag = Find_Pic.find_image_on_screen('img/物品关闭.png')
    enter_tag = Find_Pic.find_image_on_screen('img/确定.png')
    guan_bi_bag_tag = Find_Pic.find_image_on_screen('img/包裹关闭.png')
    guan_bi_jiao_tag = Find_Pic.find_image_on_screen('img/关闭交易行.png')
    if guan_bi_tag:
        move_click(guan_bi_tag[0], guan_bi_tag[1])
    if enter_tag:
        move_click(enter_tag[0], enter_tag[1])
    if guan_bi_bag_tag:
        move_click(guan_bi_bag_tag[0], guan_bi_bag_tag[1])
    if guan_bi_jiao_tag:
        move_click(guan_bi_jiao_tag[0], guan_bi_bag_tag[1])


def auto_monster(monster_num=7):
    start_coodr = re_number.get_current_coordinate()
    close_monster_tag = 0
    while True:
        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:
            break
        time.sleep(3)
        guan_bi()
        far_master, close_monster = Find_Pic.find_and_process_targets()
        # print(far_master)
        # 判断是否有怪
        if len(close_monster) < 7:

            if far_master:
                click_monster(far_master[0][0], far_master[0][1] + 46)
                close_monster_tag = 0

        click_zidong()
        current_coodr = re_number.get_current_coordinate()
        if current_coodr != start_coodr:
            close_monster_tag += 1
            print(f'第{close_monster_tag}没有发现怪物')
            start_coodr = current_coodr
        else:
            close_monster_tag =0
        if close_monster_tag > monster_num:
            break

def auto_monster_1(monster_num=7):
    start_coodr = re_number.get_current_coordinate()
    close_monster_tag = 0
    while True:
        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:
            break
        time.sleep(3)
        guan_bi()
        far_master, close_monster = Find_Pic.find_and_process_targets()
        # print(far_master)
        # 判断是否有怪
        if len(close_monster) < 7:

            if far_master:
                click_monster(far_master[0][0], far_master[0][1] + 46)
                close_monster_tag = 0

        click_zidong()
        red = Find_Pic.find_red_color()
        if not red:
            close_monster_tag += 1
        else:
            close_monster_tag = 0
        if close_monster_tag > monster_num:
            break

def eat_yuan_bao():
    # go_home()
    time.sleep(0.5)
    move_pic_click_left('img/包裹.png')
    time.sleep(0.5)
    move_pic_click_left('img/整理.png')
    time.sleep(1)
    res = Find_Pic.find_all_images_on_screen('img/元宝.png', confidence=0.95)
    res_lingqi = Find_Pic.find_all_images_on_screen('img/灵气.png', confidence=0.95)
    res_jinyan_1 = Find_Pic.find_all_images_on_screen('img/经验卷1.png', confidence=0.95)
    res_jinyan_2 = Find_Pic.find_all_images_on_screen('img/经验卷2.png', confidence=0.95)
    if res:
        for i in res:
            move_click_right(i[0], i[1])
    if res_lingqi:
        for i in res_lingqi:
            move_click_right(i[0], i[1])
    if res_jinyan_1:
        for i in res_jinyan_1:
            move_click_right(i[0], i[1])
    if res_jinyan_2:
        for i in res_jinyan_1:
            move_click_right(i[0], i[1])
    move_pic_click_left('img/整理.png')
    time.sleep(1)
    res = Find_Pic.find_all_images_on_screen('img/元宝.png', confidence=0.95)
    res_lingqi = Find_Pic.find_all_images_on_screen('img/灵气.png', confidence=0.95)
    res_jinyan_1 = Find_Pic.find_all_images_on_screen('img/经验卷1.png', confidence=0.95)
    res_jinyan_2 = Find_Pic.find_all_images_on_screen('img/经验卷2.png', confidence=0.95)
    if res:
        for i in res:
            move_click_right(i[0], i[1])
    if res_lingqi:
        for i in res_lingqi:
            move_click_right(i[0], i[1])
    if res_jinyan_1:
        for i in res_jinyan_1:
            move_click_right(i[0], i[1])
    if res_jinyan_2:
        for i in res_jinyan_1:
            move_click_right(i[0], i[1])
    time.sleep(0.5)
    move_pic_click_left('img/包裹关闭.png')

def continue_auto_monster():



    far_master, close_monster = Find_Pic.find_and_process_targets()
    # print(far_master)
    # 判断是否有怪


    if len(close_monster) < 7:

        if far_master:
            click_monster(far_master[0][0], far_master[0][1] + 46)
    click_zidong()
    guan_bi()

def kai_kuangbao():
    kuangbao = Find_Pic.find_image_on_screen('img/狂暴没了.png')
    if kuangbao:
        enter_k = Find_Pic.find_image_on_screen('img/狂暴确定.png')

        move_click(enter_k[0], enter_k[1])
        guan_bi()
        time.sleep(0.5)
        re_number.move_to_target((339, 331))
        move_pic_click('img/开狂暴NPC.png')
        move_pic_click('img/开启狂暴之力.png')




if __name__ == '__main__':
    activate_game_window(default_title)
    time.sleep(3)
    eat_yuan_bao()
    # auto_monster()
    # use_random()
