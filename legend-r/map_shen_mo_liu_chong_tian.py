import time
from os import times

import opration, re_number, Find_Pic


def go_shen_mo1():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/神魔六重地.png')
    opration.move_pic_click('img/高级传送/神魔之地-大神魔下.png')
    opration.click_zidong()

def go_shen_mo2():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/神魔六重地.png')
    opration.move_pic_click('img/高级传送/神魔之地-大神魔下.png')
    re_number.move_to_target((121, 115))
    opration.move_pic_click('img/高级传送/神魔1下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    opration.click_zidong()


def go_shen_mo3():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/神魔六重地.png')
    opration.move_pic_click('img/高级传送/神魔之地-大神魔下.png')
    re_number.move_to_target((121, 115))
    opration.move_pic_click('img/高级传送/神魔1下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((107, 106))
    opration.move_pic_click('img/高级传送/神魔2下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    opration.click_zidong()


def go_shen_mo4():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/神魔六重地.png')
    opration.move_pic_click('img/高级传送/神魔之地-大神魔下.png')
    re_number.move_to_target((121, 115))
    opration.move_pic_click('img/高级传送/神魔1下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((107, 106))
    opration.move_pic_click('img/高级传送/神魔2下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((89, 91))
    opration.move_pic_click('img/高级传送/神魔3下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    opration.click_zidong()


def go_shen_mo5():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/神魔六重地.png')
    opration.move_pic_click('img/高级传送/神魔之地-大神魔下.png')
    re_number.move_to_target((121, 115))
    opration.move_pic_click('img/高级传送/神魔1下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((107, 106))
    opration.move_pic_click('img/高级传送/神魔2下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((89, 91))
    opration.move_pic_click('img/高级传送/神魔3下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((99, 69))
    opration.move_pic_click('img/高级传送/神魔4下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    opration.click_zidong()


def go_shen_mo6():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/神魔六重地.png')
    opration.move_pic_click('img/高级传送/神魔之地-大神魔下.png')
    re_number.move_to_target((121, 115))
    opration.move_pic_click('img/高级传送/神魔1下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((107, 106))
    opration.move_pic_click('img/高级传送/神魔2下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((89, 91))
    opration.move_pic_click('img/高级传送/神魔3下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((99, 69))
    opration.move_pic_click('img/高级传送/神魔4下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    re_number.move_to_target((139, 62))
    opration.move_pic_click('img/高级传送/神魔5下层.png')
    opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    opration.click_zidong()


def is_monster(x, y):
    # 1 27, 18
    while True:
        time.sleep(2)

        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:
            break

        result = Find_Pic.find_all_images_on_screen('img/怪物.png', region=(300, 183, 516, 324))
        if len(result) == 1:
            re_number.move_to_target((x, y))
            result = Find_Pic.find_red_color()
            if not result:

                break
        opration.continue_auto_monster()




def go_shen_mo_mi_jing_6():
    # opration.go_home()
    # opration.move_pic_click('img/小秘书.png')
    # opration.move_pic_click('img/特殊传送.png')
    # opration.move_pic_click('img/高级传送/神魔六重地.png')
    # opration.move_pic_click('img/高级传送/神魔之地-大神魔下.png')
    #
    # # 一层
    # mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    # if not mengchong_tag:
    #
    #     re_number.move_to_target((121, 115))
    #     opration.move_pic_click('img/高级传送/神魔1下层.png')
    #     opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    #
    # # 二层
    # mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    # if not mengchong_tag:
    #     re_number.move_to_target((107, 106))
    #     opration.move_pic_click('img/高级传送/神魔2下层.png')
    #     opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    #
    # # 三层
    # mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    # if not mengchong_tag:
    #     re_number.move_to_target((89, 91))
    #     opration.move_pic_click('img/高级传送/神魔3下层.png')
    #     opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
    #
    # # 秘境
    # mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    # if not mengchong_tag:
    #     re_number.move_to_target((99, 69))
    #
    #     opration.move_pic_click('img/高级传送/神魔秘境.png')
    #     opration.move_pic_click('img/高级传送/神魔秘境-前往探索.png')
    #
    # # 第一个框
    # mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    # if not mengchong_tag:
    #     re_number.move_to_target((30, 15))
    #     time.sleep(1)
    #     red = Find_Pic.find_red_color()
    #     if red:
    #         opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
    #         opration.move_pic_click('img/高级传送/神魔秘境-我要进入.png')
    #         opration.click_zidong()
    #         is_monster(29, 18)
    #         opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
    #         opration.move_pic_click('img/高级传送/神魔秘境-返回.png')


    # 第二个框
    mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    if not mengchong_tag:
        re_number.move_to_target((47, 15))
        # 2个框
        time.sleep(1)
        red = Find_Pic.find_red_color()
        if red:
            opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
            opration.move_pic_click('img/高级传送/神魔秘境-我要进入.png')
            opration.click_zidong()
            is_monster(47, 19)
            opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
            opration.move_pic_click('img/高级传送/神魔秘境-返回.png')

    # 第三个框
    mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    if not mengchong_tag:
        re_number.move_to_target((29, 35))
        # 一3个框
        time.sleep(1)
        red = Find_Pic.find_red_color()
        if red:
            opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
            opration.move_pic_click('img/高级传送/神魔秘境-我要进入.png')
            opration.click_zidong()
            is_monster(30, 33)
            opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
            opration.move_pic_click('img/高级传送/神魔秘境-返回.png')


    # 第四个框
    mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    if not mengchong_tag:
        re_number.move_to_target((49, 33))
        time.sleep(1)
        red = Find_Pic.find_red_color()
        if red:
            # 一4个框
            opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
            opration.move_pic_click('img/高级传送/神魔秘境-我要进入.png')
            opration.click_zidong()
            is_monster(50, 36)
            opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
            opration.move_pic_click('img/高级传送/神魔秘境-返回.png')


    # 第五个框
    mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    if not mengchong_tag:
        re_number.move_to_target((29, 51))
        # 一5个框
        opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
        opration.move_pic_click('img/高级传送/神魔秘境-我要进入.png')
        opration.click_zidong()
        is_monster(29,54)
        opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
        opration.move_pic_click('img/高级传送/神魔秘境-返回.png')

    # 第六个框
    mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    if not mengchong_tag:
        re_number.move_to_target((49, 51))
        # 一6个框
        opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
        opration.move_pic_click('img/高级传送/神魔秘境-我要进入.png')
        opration.click_zidong()
        is_monster(49,54)
        opration.move_pic_click_jia('img/高级传送/神魔秘境-秘境使者.png')
        opration.move_pic_click('img/高级传送/神魔秘境-返回.png')

    # 去神魔六层
    mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
    if not mengchong_tag:

        re_number.move_to_target((19, 13))
        opration.move_pic_click('img/高级传送/神魔秘境-我要返回4层.png')
        opration.move_pic_click('img/高级传送/神魔秘境-我要返回4层-确定.png')

        # 去神魔6
        re_number.move_to_target((99, 69))
        opration.move_pic_click('img/高级传送/神魔4下层.png')
        opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
        re_number.move_to_target((139, 62))
        opration.move_pic_click('img/高级传送/神魔5下层.png')
        opration.move_pic_click('img/高级传送/神魔之地-神魔进入.png')
        opration.click_zidong()
        opration.auto_monster()



if __name__ == '__main__':
    go_shen_mo_mi_jing_6()

