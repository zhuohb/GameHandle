import time

import global_vars
from game_info import RoleConfig
from utils import adb_util
from utils import game_util


def process(ip, game_config: RoleConfig):
    print('----- 开始公会任务 -----')
    if not game_util.into_desktop(ip):
        return False
    # 检测桌面 点击菜单
    if not game_util.loop_match_click_area(ip, global_vars.模板_桌面_创建队伍, *global_vars.坐标_菜单):
        print('报错1')
        return False
    # 检测个人主页,点击公会
    if not game_util.loop_match_click_area(ip, global_vars.模板_菜单_个人主页, *global_vars.坐标_菜单_公会):
        print('报错2')
        return False
    # 检测公会主页
    if not game_util.loop_match(ip, global_vars.模板_公会_主页):
        print('报错3')
        return False
    # 检查是否加入公会
    temp_list = [global_vars.模板_公会_加入公会, global_vars.模板_公会_公会信息]
    for e in range(10):
        multiple_pic = game_util.find_pic_s(ip, temp_list)
        if global_vars.模板_公会_公会信息 in multiple_pic:
            #  已加入公会, 进行各种公会任务
            execute_tasks(ip, game_config)
            return True
        elif global_vars.模板_公会_加入公会 in multiple_pic:
            # 还未加入公会, 进行加入公会的操作
            join_guild(ip)
            return True
        else:
            print("未检测到公会相关模板,循环等待中")
            time.sleep(1)
    print('----- 公会任务超出循环次数 -----')
    return False


def execute_tasks(ip, game_config: RoleConfig):
    print("执行各种公会任务")
    # 等待自动签到
    time.sleep(3)
    # 领取签到奖励
    adb_util.click(ip, 1159, 110, 50, 20)
    # 领取公会任务奖励
    if game_config.isGhrwlq:
        # 公会_任务
        adb_util.click(ip, 35, 477, 85, 25)
        # 公会_任务_全部领取
        adb_util.click(ip, 1123, 667, 85, 20)
        # 公会_任务_每周
        adb_util.click(ip, 448, 106, 90, 25)
        # 公会_任务_全部领取
        adb_util.click(ip, 1123, 667, 85, 20)

    game_util.close_all(ip)


# 有些步骤没有做判断,就先将就
def join_guild(ip):
    print("执行加入公会操作")
    # 点击加入公会
    adb_util.click(ip, 547, 353, 200, 140)
    # 查找公会目录模板
    pic = game_util.loop_match(ip, global_vars.模板_公会_公会目录)
    if not pic:
        return
    # 点击公会目录
    adb_util.click(ip, pic[global_vars.模板_公会_公会目录][0], pic[global_vars.模板_公会_公会目录][1], 70, 20)
    # 点击快速加入
    adb_util.click(ip, 646, 668, 100, 30)
    # 确定加入
    adb_util.click(ip, 742, 515, 100, 30)
    # 检查是否成功加入公会
    if game_util.loop_match(ip, global_vars.模板_公会_公会信息):
        game_util.close_all(ip)
    else:
        print("加入公会失败")
