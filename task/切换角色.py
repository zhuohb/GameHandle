import time
from utils import adb_util
from utils import game_util
import global_vars


def process(ip):
    print('----- 开始切换角色 -----')
    # todo 判断角色索引是否大于角色总数

    # 从桌面点击菜单
    if not game_util.loop_match_click_area(ip, global_vars.模板_桌面_创建队伍, 1220, 23, 30, 30):
        print('----- 切换角色步骤1失败 -----')
        return False
    # 在菜单中点击更改角色按钮 todo 应该改为loop_match_click_area
    adb_util.click(ip, 1157, 643, 35, 35)
    # 检测更改角色的主页
    if not game_util.loop_match(ip, global_vars.模板_更改角色_主页):
        print('----- 切换角色步骤2失败 -----')
        return False

    # todo 如果角色索引为1,那么当前角色必须为主力,否则执行切换动作

    # 开始切换角色 在更改角色的主页点击选择角色  todo 应该改为loop_match_click_area
    adb_util.click(ip, 313, 630, 95, 25)
    # 在角色列表检测游戏开始
    if not game_util.loop_match(ip, global_vars.模板_角色列表_游戏开始):
        print('----- 切换角色步骤3失败 -----')
        return False
    # 根据角色索引,计算指定角色所在的页码
    # 根据角色索引,计算指定角色在相应页码中的位置 即1-7的位置
    # 拿到对应的坐标
    # 在角色列表选择指定角色
    # 10次循环后仍旧找不到指定的角色就停止流程

    print('----- 结束切换角色 -----')
    return False
