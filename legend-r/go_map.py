import time

import opration, Find_Pic, re_number, map_huashan, map_qi_yuan_sheng_di
import map_long_zhi_ling_yu

import map_shen_mo_liu_chong_tian
def go_huo_long3():

    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/火龙洞直飞.png')
    opration.move_pic_click('img/高级传送/火龙洞3层.png')
    opration.click_zidong()

def go_huo_long4():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/火龙洞直飞.png')
    opration.move_pic_click('img/高级传送/火龙洞4层.png')
    opration.click_zidong()

def go_huo_long5():
    # opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/火龙洞直飞.png')
    opration.move_pic_click('img/高级传送/火龙洞5层.png')
    opration.click_zidong()

def go_huo_long6():
    # opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/火龙洞直飞.png')
    opration.move_pic_click('img/高级传送/火龙洞6层.png')
    opration.click_zidong()

def go_huo_long7():
    # opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/火龙洞直飞.png')
    opration.move_pic_click('img/高级传送/火龙洞7层.png')
    opration.click_zidong()

def go_gu_du_2(id = 2):
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    if id == 2:
        opration.move_pic_click('img/高级传送/孤独2.png')
    elif id == 1:
        opration.move_pic_click('img/高级传送/孤独1.png')
    opration.move_pic_click('img/高级传送/我要进入.png')
    opration.kai_kuangbao()
    opration.click_zidong()




def go_shen_long_ling_di():
    opration.go_home()
    opration.move_pic_click('img/小秘书.png')
    opration.move_pic_click('img/特殊传送.png')
    opration.move_pic_click('img/高级传送/神龙的圣地.png')
    opration.move_pic_click('img/高级传送/2w元宝进入.png')
    opration.click_zidong()






def gua_ji_huo_long():

        opration.go_home()
        go_huo_long4()
        opration.auto_monster()
        print('火龙4刷完')
        go_huo_long5()
        opration.auto_monster()
        print('火龙5刷完')
        go_huo_long6()
        opration.auto_monster()
        print('火龙6刷完')
        go_huo_long7()
        opration.auto_monster()
        print('火龙7刷完')
        go_huo_long3()
        re_number.move_to_target((48, 81))
        opration.click_zidong()
        opration.auto_monster()
        print('火龙3刷完')
        opration.go_home()

def main1():
    opration.activate_game_window(window_title="热血华山15区(16:00)")
    while True:
        time.sleep(4)
        # opration.kai_kuangbao()
        opration.guan_bi()
        current_time = time.localtime()
        if 55 <= current_time.tm_min < 58:
            map_qi_yuan_sheng_di.gj_shang_gu_yi_ji()
            if current_time.tm_hour in [3, 6, 9, 12, 15, 18]:
                map_huashan.gj_dian_feng()
            map_huashan.gj_hua_shan()
            opration.eat_yuan_bao()
            # gua_ji_huo_long()
            # opration.eat_yuan_bao()
            map_qi_yuan_sheng_di.gj_shen_di_shen3()
            map_shen_mo_liu_chong_tian.go_shen_mo_mi_jing_6()

        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:

            go_gu_du_2(1)
        opration.guan_bi()
        opration.continue_auto_monster()


def main2():
    opration.activate_game_window(window_title="热血华山5区(16:00)")
    while True:
        time.sleep(4)
        opration.guan_bi()


        mengchong_tag = Find_Pic.find_image_on_screen('img/盟重城.png')
        if mengchong_tag:
            map_long_zhi_ling_yu.gj_long_ling_di_xi()
        opration.guan_bi()
        opration.continue_auto_monster()



if __name__ == '__main__':
    pass

