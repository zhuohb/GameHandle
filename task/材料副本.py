import time
from utils import adb_util
from utils import game_util
import global_vars


def process(ip):
    print('----- 开始材料副本 -----')
    # 从桌面到日常玩法
    if not game_util.into_rcwf_from_desktop(ip):
        return False
    time.sleep(0.5)
    # 从日常玩法到相应副本
    if not game_util.into_fb_from_rcwf(ip, global_vars.模板_材料副本_入口, global_vars.坐标_材料副本_入口):
        return False
    time.sleep(0.5)
    # 确定主页
    if not game_util.loop_match(ip, global_vars.模板_材料副本_主页):
        return False
    time.sleep(0.5)
    # 点击入场
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_入场, 45, 25):
        print('副本报错1')
        return False
    time.sleep(0.5)
    # 点击确定
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_确定, 45, 25):
        print('副本报错2')
        return False
    time.sleep(0.5)
    # 再次点击确定
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_确定, 45, 25):
        print('副本报错3')
        return False
    # 等待结束
    for i in range(5 * 60):
        pic_info = game_util.find_multiple_pic(ip, (global_vars.模板_副本通用_离开, global_vars.模板_副本通用_放弃))
        if pic_info:
            # 隔一秒再检测一遍,避免因为动画造成定位错误
            time.sleep(1)
            pic_info_2 = game_util.find_multiple_pic(ip, (global_vars.模板_副本通用_离开, global_vars.模板_副本通用_放弃))
            if pic_info_2:
                pic = pic_info_2[0]
                adb_util.click(ip, pic[1], pic[2], 60, 20)
                time.sleep(1)
                print('----- 结束材料副本 -----')
                return True
        else:
            time.sleep(1)
    print('----- 材料副本超出循环次数 -----')
    return False
