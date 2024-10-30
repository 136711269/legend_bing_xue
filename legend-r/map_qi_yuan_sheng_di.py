import time

import opration, re_number


def gj_shang_gu_yi_ji():
    current_time = time.localtime()
    if current_time.tm_hour in [3, 7,11, 15, 19, 23]:
        opration.go_home()
        opration.move_pic_click('img/小秘书.png')
        opration.move_pic_click('img/特殊传送.png')
        opration.move_pic_click('img/高级传送/上古遗迹.png')
        opration.move_pic_click('img/高级传送/上古-2万元宝进入.png')
        re_number.move_to_target((74, 87))
        opration.click_zidong()
        opration.auto_monster()


def gj_shen_di_shen():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/冰雪之城/冰雪之城.png')
    re_number.move_to_target((164, 63))
    opration.move_pic_click('img/冰雪之城/起源圣地.png')
    opration.move_pic_click('img/冰雪之城/圣地神.png', confidence=0.8)
    opration.move_pic_click('img/冰雪之城/圣地神-我要前往.png',confidence=0.7)
    re_number.move_to_target((60, 68))
    opration.click_zidong()
    opration.auto_monster()
    opration.go_home()


def gj_shen_di_shen2():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/冰雪之城/冰雪之城.png')
    re_number.move_to_target((164, 63))
    opration.move_pic_click('img/冰雪之城/起源圣地.png')
    opration.move_pic_click('img/冰雪之城/进入圣地2.png')
    opration.click_zidong()
    opration.auto_monster()


def gj_shen_di_shen1():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/冰雪之城/冰雪之城.png')
    re_number.move_to_target((164, 63))
    opration.move_pic_click('img/冰雪之城/起源圣地.png')
    opration.move_pic_click('img/冰雪之城/进入圣地1.png')
    opration.click_zidong()
    opration.auto_monster()




def gj_shen_di_shen3():
    current_time = time.localtime()
    gj_shen_di_shen()
    if current_time.tm_hour in [3, 9,  15, 22]:
        gj_shen_di_shen2()
        gj_shen_di_shen1()
if __name__ == '__main__':
    # gj_shen_di_shen2()
    # gj_shen_di_shen1()
    gj_shen_di_shen()