import time

import global_vars
from game_info import GlobalConfig
from utils import game_util, adb_util


def process(ip, global_config: GlobalConfig):
    if global_config.isHdMrqd:
        活动_每日签到(ip)
    if global_config.isCwjy:
        宠物任务(ip)
    if global_config.isLqMzczrw:
        领取每周成长(ip)


def 活动_每日签到(ip):
    pass


def 宠物任务(ip):
    pass




def 领取每周成长(ip):
    pass
