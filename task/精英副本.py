import time
from utils import adb_util
from utils import game_util
import global_vars


def process(ip):
    print('----- 开始精英副本 -----')
    # 从桌面到日常玩法
    if not game_util.into_rcwf_from_desktop(ip):
        return False
    # 从日常玩法到相应副本
    if not game_util.into_fb_from_rcwf(ip, global_vars.模板_精英副本_入口, global_vars.坐标_精英副本_入口):
        return False
    # 确定主页
    if not game_util.loop_match(ip, global_vars.模板_精英副本_主页):
        return False
    # 是否已完成
    if is_complete(ip):
        return True
    # 点击确定
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_确定, 45, 25):
        print('副本报错2')
        return False
    # 等待结束
    for i in range(10 * 60):
        pic_info = game_util.find_pic(ip, global_vars.模板_副本通用_离开)
        if pic_info:
            # 隔一秒再检测一遍,避免因为动画造成定位错误
            time.sleep(1)
            pic_info_2 = game_util.find_pic(ip, global_vars.模板_副本通用_离开)
            if pic_info_2:
                adb_util.click(ip, pic_info_2[1], pic_info_2[2], 60, 20)
                time.sleep(1)
                print('----- 结束精英副本 -----')
                return True
        else:
            time.sleep(1)
    print('----- 副本超出循环次数 -----')
    return False


def is_complete(ip):
    """
    是否完成副本
    :param ip:
    :return:
    """
    temp_list = [global_vars.模板_副本通用_快速组队, global_vars.模板_副本通用_快速组队_已完成]
    for e in range(10):
        multiple_pic = game_util.find_pic_s(ip, temp_list)
        if global_vars.模板_副本通用_快速组队_已完成 in multiple_pic:
            print('副本已完成')
            return True
        elif global_vars.模板_副本通用_快速组队 in multiple_pic:
            pic = multiple_pic[global_vars.模板_副本通用_快速组队]
            adb_util.click(ip, pic[0], pic[1], 90, 25)
            return False
        else:
            time.sleep(1)
