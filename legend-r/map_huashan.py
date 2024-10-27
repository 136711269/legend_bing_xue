import time

import opration, re_number


def gj_hua_shan():
    current_time = time.localtime()
    opration.go_home()
    re_number.move_to_target((330, 325))
    opration.move_pic_click('img/盟重地图/热血华山.png')
    opration.move_pic_click('img/盟重地图/华山-我要进去挑战.png')
    re_number.move_to_target((7, 11))
    opration.move_up_left(3)
    if current_time.tm_hour in [3, 9, 15]:
        re_number.move_to_target((19, 20))
    else:
        re_number.move_to_target((37, 38))

    opration.click_zidong()
    opration.auto_monster(3)

    opration.go_home()


def gj_dian_feng():
    opration.go_home()
    re_number.move_to_target((330, 325))
    opration.move_pic_click('img/盟重地图/巅峰之战.png')
    opration.move_pic_click('img/盟重地图/巅峰-2000元宝前往.png')
    re_number.move_to_target((42, 69))
    opration.click_zidong()
    opration.auto_monster()
    opration.go_home()

    # re_number.move_to_target((48, 81))
    # opration.move_pic_click('img/特殊传送.png')
    # opration.move_pic_click('img/高级传送/火龙洞直飞.png')
    # opration.move_pic_click('img/高级传送/火龙洞3层.png')
    # opration.move_pic_click('img/自动挂机.png')



if __name__ == '__main__':
    pass