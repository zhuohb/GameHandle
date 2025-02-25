import global_vars
from game_info import GlobalConfig
from utils import game_util


def process(ip, global_config: GlobalConfig):
    if global_config.isHdMrqd:
        活动_每日签到(ip)
    if global_config.isCwjy:
        宠物任务(ip)
    if global_config.isLqMzczrw:
        领取每周成长(ip)
    if global_config.isLqTyyj:
        领取通用邮件(ip)


def 活动_每日签到(ip):
    pass


def 宠物任务(ip):
    pass


def 领取通用邮件(ip):
    if not game_util.into_desktop(ip):
        return False
    if not game_util.loop_match_click_area(ip, global_vars.模板_桌面_创建队伍, *global_vars.坐标_菜单):
        print('loop_match_click_area 步骤1失败')
        return False
    if not game_util.loop_match_click_area(ip, global_vars.模板_菜单_个人主页, *global_vars.坐标_菜单_邮件):
        print('loop_match_click_area 步骤2失败')
        return False
    if not game_util.loop_match(ip, global_vars.模板_邮件_主页):
        return False


def 领取每周成长(ip):
    pass
