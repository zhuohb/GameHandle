import threading
import time

from game_info import GameInfo, GlobalConfig, RoleConfig, SINGLE_ROLE_MODEL
from task import 材料副本, 切换角色, 公会任务, 周常副本, 领取自动战斗时间, 邮件任务
from utils import adb_util, game_util


def start(ip):
    # 角色全局配置
    global_config = GlobalConfig()
    global_config.isMrqd = True
    # 三个角色
    role_config_list = []
    for e in range(6):
        role_config = RoleConfig()
        role_config.isClfb = True
        # role_config.selectClfbType = '5'
        role_config_list.append(role_config)
    # 组装角色的配置信息
    game_info = GameInfo(31, 1, SINGLE_ROLE_MODEL, global_config, role_config_list)

    # 前置任务: 连接设备
    if not adb_util.connect(ip):
        print(f'连接设备{ip}失败')
        return
    # 前置任务: 进入桌面
    if not game_util.into_desktop(ip):
        print(f'{ip} 进入桌面失败')
        return
    # 从指定的角色索引开始
    切换角色.process(ip, game_info)

    # 到这个就开始刷了,当前角色索引小于或等于角色总数时才可以刷
    while game_info.currentRoleIndex <= game_info.roleTotal:
        role_config = role_config_list[game_info.currentRoleIndex - 1]
        公会任务.process(ip, role_config)
        邮件任务.领取个人邮件(ip)
        材料副本.process(ip, role_config)
        # 精英副本.process(ip)
        周常副本.process(ip)

        邮件任务.领取个人邮件(ip)
        领取自动战斗时间.process(ip)
        # 任务结束之后角色索引+1
        game_info.currentRoleIndex = game_info.currentRoleIndex + 1
        # 然后切换角色
        切换角色.process(ip, game_info)


if __name__ == '__main__':
    ip_list = [
        '192.168.1.70:5555',
        # '192.168.3.48:5555'
    ]
    # 加载模板图像
    game_util.load_template_images_from_directory('./image')
    # 创建线程池
    threads = []
    for item in ip_list:
        thread = threading.Thread(target=start, args=(item,))
        thread.start()
        threads.append(thread)
        time.sleep(1)

    # 等待所有线程完成
    for thread in threads:
        thread.join()
