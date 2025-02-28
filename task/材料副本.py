import time

from game_info import RoleConfig
from utils import adb_util
from utils import game_util
import global_vars


def process(ip, game_config: RoleConfig):
    print('----- 开始材料副本 -----')
    if not game_util.into_fbzy_from_desktop(ip, global_vars.模板_材料副本_入口, global_vars.模板_材料副本_主页):
        return False
    # 是否已完成
    multiple_pic = game_util.find_pic_s(ip, [global_vars.模板_副本通用_入场, global_vars.模板_副本通用_入场_已完成])
    if global_vars.模板_副本通用_入场_已完成 in multiple_pic:
        print('副本已完成')
        game_util.close_all(ip)
        return True
    elif global_vars.模板_副本通用_入场 in multiple_pic:
        # 选择副本
        if not game_config.selectClfbType == '0':
            type = global_vars.材料副本类型[game_config.selectClfbType]
            adb_util.click(ip, type[0], type[1], 90, 30)

        pic = multiple_pic[global_vars.模板_副本通用_入场]
        adb_util.click(ip, pic[0], pic[1], 90, 25)
    else:
        return False

    # 点击确定
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_确定, 45, 25):
        print('副本报错2')
        return False
    # 再次点击确定
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_确定, 45, 25):
        print('副本报错3')
        return False
    # 等待结束
    temp_list = [global_vars.模板_副本通用_离开, global_vars.模板_副本通用_放弃]
    for i in range(5 * 60):
        pic_info = game_util.find_pic_s(ip, temp_list)
        if pic_info:
            # 隔一秒再检测一遍,避免因为动画造成定位错误
            time.sleep(1)
            pic_info_2 = game_util.find_pic_s(ip, temp_list)
            if pic_info_2:
                # 取第一个key对应的value
                pic = pic_info_2[next(iter(pic_info_2))]
                adb_util.click(ip, pic[0], pic[1], 60, 20)
                print('----- 结束材料副本 -----')
                return True
        else:
            time.sleep(1)
    print('----- 材料副本超出循环次数 -----')
    return False
