import time

from fontTools.merge.util import current_time
from gitdb.util import close

import re_number
import pyautogui

import Find_Pic

coordinate = {'img/小秘书': (35, 339), 'img/高级传送':(230, 292), 'img/起源冰城':(391, 248), 'img/自动挂机':(990, 376)}

def click(x, y):
    time.sleep(1)
    pyautogui.click(x, y)
    # time.sleep(0.5)
    # pyautogui.click(x, y)

def click_monster(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()

def click_right(x, y):
    time.sleep(1)
    pyautogui.rightClick(x, y)
    # pyautogui.leftClick()


def move_click(x, y):
    time.sleep(0.5)
    pyautogui.moveTo(x, y, duration=0.1)
    time.sleep(0.5)
    pyautogui.leftClick()


def move_click_right(x, y):
    time.sleep(1)
    pyautogui.moveTo(x, y, duration=0.1)
    print(f'鼠标移动到{x,y}')
    time.sleep(0.5)
    pyautogui.rightClick()


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



def move_pic_click(pic_path):
    i = 0
    while i < 10:
        time.sleep(0.5)
        pic_tag = Find_Pic.find_image_on_screen(pic_path)
        if pic_tag:
            print(pic_path)
            move_click(pic_tag[0], pic_tag[1])
            time.sleep(0.5)
            break
        else:
            print(f'点击失败{pic_path}')
        i += 1


def move_up_left(sec):
    time.sleep(0.5)
    pyautogui.moveTo(408, 222)
    pyautogui.mouseDown()
    time.sleep(sec)
    pyautogui.mouseUp()



def click_zidong():
    zidong_tag = Find_Pic.find_image_on_screen('img/自动挂机.png')
    if zidong_tag:
        move_click(zidong_tag[0], zidong_tag[1])



def guan_bi():
    guan_bi_tag = Find_Pic.find_image_on_screen('img/物品关闭.png')
    enter_tag = Find_Pic.find_image_on_screen('img/确定.png')
    guan_bi_bag_tag = Find_Pic.find_image_on_screen('img/包裹关闭.png')
    if guan_bi_tag:
        move_click(guan_bi_tag[0], guan_bi_tag[1])
    if enter_tag:
        move_click(enter_tag[0], enter_tag[1])
    if guan_bi_bag_tag:
        move_click(guan_bi_bag_tag[0], guan_bi_bag_tag[1])


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
        if len(close_monster) < monster_num:

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
        if close_monster_tag > 7:
            break

def eat_yuan_bao():
    # go_home()
    time.sleep(0.5)
    move_pic_click_left('img/包裹.png')
    time.sleep(0.5)
    move_pic_click_left('img/整理.png')
    time.sleep(1)
    res = Find_Pic.find_all_images_on_screen('img/元宝.png', confidence=0.95)
    if res:
        for i in res:
            click_right(i[0], i[1])
    move_pic_click_left('img/整理.png')
    time.sleep(1)
    res = Find_Pic.find_all_images_on_screen('img/元宝.png')
    if res:
        for i in res:
            click_right(i[0], i[1])
    time.sleep(0.5)
    move_pic_click_left('img/包裹关闭.png')

def continue_auto_monster():


    guan_bi()
    far_master, close_monster = Find_Pic.find_and_process_targets()
    # print(far_master)
    # 判断是否有怪


    if len(close_monster) < 7:

        if far_master:
            click_monster(far_master[0][0], far_master[0][1] + 46)
    click_zidong()



if __name__ == '__main__':
    time.sleep(3)
    # eat_yuan_bao()
    # auto_monster()
    # use_random()
    random_path = '随机石数量.txt'
    write_number(random_path, 0)