import time

import global_vars
from utils import game_util, adb_util


def process(ip):
    print('开始领取自动战斗时间')
    if not game_util.into_desktop(ip):
        return False
    # 打开自动战斗
    adb_util.click(ip, 407, 645, 33, 23)
    # 点击领取
    game_util.loop_match_click_area(ip, global_vars.模板_自动战斗_主页, *global_vars.坐标_自动战斗_领取)
    game_util.close_all(ip)
    print('结束领取自动战斗时间')
    return True