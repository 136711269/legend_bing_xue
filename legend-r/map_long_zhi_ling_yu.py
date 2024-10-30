import time
from os import times

import opration, re_number, Find_Pic


def is_shen_dian():
    shen_dian_tag = Find_Pic.find_image_on_screen('img/高级传送/龙之神殿.png')
    if shen_dian_tag:
        re_number.move_to_target((13, 17))
        opration.move_up_left(3)

    else:
        pass


def gj_long_ling_di():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/龙之领域.png')

    re_number.move_to_target((10, 11))
    opration.move_up_left(3)
    opration.move_pic_click('img/自动挂机.png')
    opration.auto_monster()


def gj_long_ling_di_xi():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/龙之领域.png')
    opration.move_pic_click('img/高级传送/我要进入.png')
    start = time.time()
    while True:
        end = time.time()
        if end - start > 60:
            opration.go_home()
            break
        re_number.move_to_target((10, 11))
        opration.move_up_left(3)
        long_zhong_tag = Find_Pic.find_image_on_screen('img/高级传送/龙之领域中.png')
        if not long_zhong_tag:
            break
        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:
            break
    opration.click_zidong()
    # opration.auto_monster()


def gj_long_ling_di_bei():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/龙之领域.png')
    opration.move_pic_click('img/高级传送/我要进入.png')
    start = time.time()
    while True:
        end = time.time()
        if end - start > 60:
            opration.go_home()
            break
        re_number.move_to_target((27, 17))
        opration.move_up(3)
        long_zhong_tag = Find_Pic.find_image_on_screen('img/高级传送/龙之领域中.png')
        if not long_zhong_tag:
            break
        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:
            break
    opration.move_pic_click('img/自动挂机.png')
    # opration.auto_monster()


def gj_long_ling_di_east():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/龙之领域.png')
    opration.move_pic_click('img/高级传送/我要进入.png')
    while True:
        re_number.move_to_target((26, 28))
        opration.move_down(3)
        long_zhong_tag = Find_Pic.find_image_on_screen('img/高级传送/龙之领域中.png')
        if not long_zhong_tag:
            break
        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:
            break
    opration.move_pic_click('img/自动挂机.png')
    # opration.auto_monster()



if __name__ == '__main__':
    while True:
        time.sleep(3)
        current_time = time.localtime()
        # if 56 <= current_time.tm_min < 58:
        #     map_qi_yuan_sheng_di.gj_shang_gu_yi_ji()
        #     if current_time.tm_hour in [3, 6, 9, 12, 15, 18]:
        #         map_huashan.gj_dian_feng()
        #     map_huashan.gj_hua_shan()
        #     opration.eat_yuan_bao()
        #     # gua_ji_huo_long()
        #     # opration.eat_yuan_bao()
        #     map_qi_yuan_sheng_di.gj_shen_di_shen3()
        #     map_shen_mo_liu_chong_tian.go_shen_mo_mi_jing_6()

        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:
            gj_long_ling_di_xi()
        opration.guan_bi()
        opration.continue_auto_monster()