import sys

from game_info import GameInfo, GlobalConfig, RoleConfig, SINGLE_ROLE_MODEL
from task import 材料副本, 精英副本, 切换角色
from utils import adb_util, game_util

if __name__ == '__main__':
    ip = '192.168.1.70:5555'
    # 加载模板图像
    game_util.load_template_images_from_directory('./image')
    # 角色全局配置
    global_config = GlobalConfig()
    global_config.isMrqd = True
    # 三个角色
    role_config_list = []
    for e in range(3):
        role_config = RoleConfig()
        role_config.isClfb = True
        role_config_list.append(role_config)
    # 组装角色的配置信息
    game_info = GameInfo(3, 1, SINGLE_ROLE_MODEL, global_config, role_config_list)

    # 前置任务: 连接设备
    if not adb_util.connect(ip):
        print('连接设备失败')
        # 退出状态码为 1 表示异常退出
        sys.exit(1)
    # 前置任务: 进入桌面
    if not game_util.into_desktop(ip):
        print('进入桌面失败')
        sys.exit(1)
    # 从指定的角色索引开始
    切换角色.process(ip, game_info)


    # 到这个就开始刷了,当前角色索引小于或等于角色总数时才可以刷
    while game_info.currentRoleIndex <= game_info.roleTotal:
        # todo 还没有传入角色自己的配置
        材料副本.process(ip)
        精英副本.process(ip)
        # 任务结束之后角色索引+1
        game_info.currentRoleIndex = game_info.currentRoleIndex + 1
        # 然后切换角色
        切换角色.process(ip, game_info)
