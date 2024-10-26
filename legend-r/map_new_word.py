import opration, re_number, Find_Pic


def gj_xin_shi_jie():
    opration.go_home()
    re_number.move_to_target((299, 331))
    opration.move_pic_click('img/高级传送/新世界.png')
    opration.move_pic_click('img/高级传送/进入新世界.png')
    opration.use_random()
    opration.click_zidong()
    random_num = opration.read_number('随机石数量.txt')
    while True:
        xinshijie_tag = Find_Pic.find_image_on_screen('img/高级传送/新世界-地图.png')
        if not xinshijie_tag:
            break
        opration.auto_monster(monster_num=4)
        opration.use_random()
        random_num += 1
        if random_num > 100:
            opration.guan_bi()
            opration.buy_random()
















if __name__ == '__main__':
    gj_xin_shi_jie()
