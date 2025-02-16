from utils import game_util
import global_vars


def process(ip):
    print('----- 开始材料副本 -----')
    # 从桌面到日常玩法
    if not game_util.into_rcwf_from_desktop(ip):
        return False
    # 从日常玩法到相应副本
    if not game_util.into_fb_from_rcwf(ip, global_vars.模板_材料副本_入口, global_vars.坐标_材料副本_入口):
        return False
    # 确定主页
    if not game_util.loop_match(ip, global_vars.模板_材料副本_主页):
        return False
    # 点击入场
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_入场, 45, 25):
        print('副本报错1')
        return False
    # 点击确定
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_确定, 45, 25):
        print('副本报错2')
        return False
    # 再次点击确定
    if not game_util.loop_match_click(ip, global_vars.模板_副本通用_确定, 45, 25):
        print('副本报错2')
        return False

    print('----- 结束材料副本 -----')
