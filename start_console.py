import threading
import time

import 角色配置
from task import 材料副本, 切换角色, 公会任务, 周常副本, 领取自动战斗时间
from utils import adb_util, game_util


def start(ip, game_info):
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
    while game_info['当前角色索引'] <= game_info['角色总数']:
        role_config = game_info['角色配置列表'][game_info['当前角色索引'] - 1]
        公会任务.process(ip, role_config)
        材料副本.process(ip, role_config)
        # 精英副本.process(ip)
        周常副本.process(ip)

        领取自动战斗时间.process(ip)
        # 任务结束之后角色索引+1
        game_info['当前角色索引'] = game_info['当前角色索引'] + 1
        # 然后切换角色
        切换角色.process(ip, game_info)


if __name__ == '__main__':
    ip_list = [
        '192.168.1.126:5555', 角色配置.小黑子
        # '192.168.3.48:5555'
    ]
    # 加载模板图像
    game_util.load_template_images_from_directory('./image')
    # 创建线程池
    threads = []
    for item, config in ip_list:
        thread = threading.Thread(target=start, args=(item, config))
        thread.start()
        threads.append(thread)
        time.sleep(1)

    # 等待所有线程完成
    for thread in threads:
        thread.join()
