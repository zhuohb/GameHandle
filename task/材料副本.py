from utils import game_util
import global_vars


def process(ip):
    print('----- 开始材料副本 -----')
    if not game_util.into_rcwf_from_desktop(ip):
        return False
    if not game_util.into_fb_from_rcwf(ip, global_vars.模板_材料副本_入口, global_vars.坐标_材料副本_入口):
        return False
    print('----- 结束材料副本 -----')
