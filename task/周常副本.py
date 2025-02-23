import time
from utils import adb_util
from utils import game_util
import global_vars


def process(ip):
    print('----- 开始周常副本 -----')
    if not game_util.fb_prefix(ip, global_vars.模板_周常副本_入口, global_vars.模板_周常副本_主页):
        return False
    # 是否已完成
    temp_list = [global_vars.模板_副本通用_入场, global_vars.模板_副本通用_入场_已完成]
    multiple_pic = game_util.find_pic_s(ip, temp_list)
    if global_vars.模板_副本通用_入场_已完成 in multiple_pic:
        print('副本已完成')
        game_util.close_all(ip)
        return True
    elif global_vars.模板_副本通用_入场 in multiple_pic:
        pic = multiple_pic[global_vars.模板_副本通用_入场]
        adb_util.click(ip, pic[0], pic[1], 90, 25)
    else:
        return False

    # 点击确定
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_确定, 45, 25):
        print('副本报错2')
        return False
    # 等待结束
    for i in range(5 * 60):
        pic_info = game_util.find_pic(ip, global_vars.模板_副本通用_离开)
        if pic_info:
            # 隔一秒再检测一遍,避免因为动画造成定位错误
            time.sleep(1)
            pic_info_2 = game_util.find_pic(ip, global_vars.模板_副本通用_离开)
            if pic_info_2:
                pic = pic_info_2[global_vars.模板_副本通用_离开]
                adb_util.click(ip, pic[0], pic[1], 60, 20)
                print('----- 结束周常副本 -----')
                return True
        else:
            time.sleep(1)
    print('----- 周常副本超出循环次数 -----')
    return False
