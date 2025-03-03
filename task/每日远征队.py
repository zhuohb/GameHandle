import time

import global_vars
from utils import game_util, adb_util


def process(ip):
    print('开始每日远征队任务')
    item1 = [global_vars.模板_副本通用_快速组队, global_vars.模板_副本通用_快速组队_已完成]
    # 今天星期几
    today = time.localtime().tm_wday
    # 今天的远征队
    for yzd in global_vars.每日远征队[today]:
        # 进入远征队
        if not game_util.into_fbzy_from_desktop(ip, global_vars.模板_远征队_入口, global_vars.模板_远征队_主页):
            return False
        # 每个领主只能打2次
        for _ in range(2):
            game_util.loop_match_click(ip, *yzd)
            # 是否已完成
            multiple_pic = game_util.find_pic_s(ip, item1)
            if global_vars.模板_副本通用_快速组队_已完成 in multiple_pic:
                print('当前远征领主已完成,下一个')
                break
            elif global_vars.模板_副本通用_快速组队 in multiple_pic:
                # 点击快速组队
                pic = multiple_pic[global_vars.模板_副本通用_快速组队]
                adb_util.click(ip, pic[0], pic[1], 90, 25)
                # 等待完成
                if wait_completion(ip):
                    break
            else:
                print('当前远征领主未找到,重试')
                return False
    print('结束每日远征队任务')
    return True


def wait_completion(ip):
    item2 = [global_vars.模板_远征队_副本内再次挑战, global_vars.模板_远征队_副本内已完成]
    for _ in range(60 * 5):
        wait_pic = game_util.find_pic_s(ip, item2)
        if global_vars.模板_远征队_副本内再次挑战 in wait_pic:
            # 点击再次挑战
            pic = wait_pic[global_vars.模板_远征队_副本内再次挑战]
            adb_util.click(ip, pic[0], pic[1], 90, 25)
        elif global_vars.模板_远征队_副本内已完成 in wait_pic:
            print('远征领主已完成')
            return True
        else:
            time.sleep(1)
