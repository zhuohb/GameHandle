import global_vars
from game_info import GameInfo
from utils import adb_util
from utils import game_util


def process(ip, game_info: GameInfo):
    print('----- 开始切换角色 -----')
    # 当前角色的索引

    # 判断角色索引是否大于角色总数
    if game_info.currentRoleIndex > game_info.roleTotal:
        print("角色索引大于角色总数,退出流程")
        return False
    # 从桌面点击菜单
    if not game_util.loop_match_click_area(ip, global_vars.模板_桌面_创建队伍, 1220, 23, 30, 30):
        print('----- 切换角色步骤1失败 -----')
        return False
    # 在菜单中点击更改角色按钮
    if not game_util.loop_match_click_area(ip, global_vars.模板_菜单_个人主页, 1157, 643, 35, 35):
        print('----- 切换角色步骤2失败 -----')
        return False
    # 检测更改角色的主页
    if not game_util.loop_match(ip, global_vars.模板_更改角色_主页):
        print('----- 切换角色步骤3失败 -----')
        return False

    # 如果角色索引为1,那么当前角色必须为主力,否则执行切换动作
    if game_info.currentRoleIndex == 1:
        pic = game_util.loop_match(ip, global_vars.模板_更改角色_主页_主力)
        if pic and pic[global_vars.模板_更改角色_主页_主力][0] > 970 and pic[global_vars.模板_更改角色_主页_主力][1] < 175:
            print(" 当前角色是主力,可以开始刷了")
            game_util.close_all(ip)
            return True

    # 开始切换角色 在更改角色的主页点击选择角色
    adb_util.click(ip, 313, 630, 95, 25)
    # 在角色列表检测游戏开始
    if not game_util.loop_match(ip, global_vars.模板_角色列表_游戏开始):
        print('----- 切换角色步骤4失败 -----')
        return False
    # 根据角色索引,计算指定角色所在的页码
    page_num = game_util.calculate_role_page(game_info.currentRoleIndex, game_info.rolePerPageCount)
    # 根据角色索引,计算指定角色在相应页码中的位置 即1-7的位置
    position_index = game_util.calculate_current_role_in_current_page_index(game_info.currentRoleIndex, game_info.rolePerPageCount)
    # 拿到对应的坐标
    position_area = global_vars.role_position[position_index]
    # 在角色列表选择指定角色
    for e in range(10):
        pic = game_util.find_pic(ip, global_vars.role_page_num[page_num])
        if pic:
            # 在指定角色的页码了, 选中指定的角色
            adb_util.click(ip, *position_area)
            # 点击游戏开始
            adb_util.click(ip, 1072, 654, 100, 25)
            print('----- 结束切换角色 -----')
            return True
        else:
            # 当找不到角色页时切换列表
            adb_util.click(ip, 837, 337, 25, 40)

    # 10次循环后仍旧找不到指定的角色就停止流程
    print('----- 副本超出循环次数 -----')
    return False
