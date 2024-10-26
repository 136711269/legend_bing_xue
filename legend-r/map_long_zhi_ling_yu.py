import opration, re_number


def gj_long_ling_di():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/龙之领域.png')
    opration.move_pic_click('img/高级传送/我要进入.png')
    re_number.move_to_target((10, 11))
    opration.move_up_left(3)
    opration.move_pic_click('img/自动挂机.png')
    opration.auto_monster()


if __name__ == '__main__':
    gj_long_ling_di()