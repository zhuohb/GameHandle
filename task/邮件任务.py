import time

import global_vars
from utils import game_util, adb_util


def 领取通用邮件(ip):
    print('领取通用邮件')
    if not game_util.into_desktop(ip):
        return False
    if not game_util.loop_match_click_area(ip, global_vars.模板_桌面_创建队伍, *global_vars.坐标_菜单):
        print('步骤1失败')
        return False
    if not game_util.loop_match_click_area(ip, global_vars.模板_菜单_个人主页, *global_vars.坐标_菜单_邮件):
        print('步骤2失败')
        return False
    if not game_util.loop_match(ip, global_vars.模板_邮件_主页):
        return False

    return handle(ip)


def 领取个人邮件(ip):
    print('领取个人邮件')
    if not game_util.into_desktop(ip):
        return False
    if not game_util.loop_match_click_area(ip, global_vars.模板_桌面_创建队伍, *global_vars.坐标_菜单):
        print('步骤1失败')
        return False
    if not game_util.loop_match_click_area(ip, global_vars.模板_菜单_个人主页, *global_vars.坐标_菜单_邮件):
        print('步骤2失败')
        return False
    # todo 个人坐标未测量
    if not game_util.loop_match_click_area(ip, global_vars.模板_邮件_主页, 0, 0, 0, 0):
        return False
    if not game_util.loop_match(ip, global_vars.模板_邮件_个人):
        return False

    return handle(ip)


def handle(ip):
    temp_list = [global_vars.模板_邮件_无邮件, global_vars.模板_邮件_全部领取, global_vars.模板_邮件_勾选框, global_vars.模板_邮件_确认,
                 global_vars.模板_邮件_确定, global_vars.模板_邮件_删除, global_vars.模板_邮件_已全部领取]
    for e in range(10):
        pic_info = game_util.find_pic_s(ip, temp_list)
        if pic_info:
            if global_vars.模板_邮件_无邮件 in pic_info:
                print('无邮件')
                game_util.close_all(ip)
                return True
            elif global_vars.模板_邮件_全部领取 in pic_info:
                pic = pic_info[global_vars.模板_邮件_全部领取]
                adb_util.click(ip, pic[0], pic[1], 90, 30)
            elif global_vars.模板_邮件_勾选框 in pic_info:
                adb_util.click(ip, 551, 530, 30, 25)
            elif global_vars.模板_邮件_确认 in pic_info:
                pic = pic_info[global_vars.模板_邮件_确认]
                adb_util.click(ip, pic[0], pic[1], 60, 30)
            elif global_vars.模板_邮件_确定 in pic_info:
                pic = pic_info[global_vars.模板_邮件_确定]
                adb_util.click(ip, pic[0], pic[1], 60, 30)
            elif global_vars.模板_邮件_删除 in pic_info:
                pic = pic_info[global_vars.模板_邮件_删除]
                adb_util.click(ip, pic[0], pic[1], 50, 50)
            elif global_vars.模板_邮件_已全部领取 in pic_info:
                game_util.close_all(ip)
                print('领取通用邮件成功')
                return True
            else:
                time.sleep(1)
    print('领取通用邮件超出循环次数')
