from task import 全局任务, 邮件任务, 领取自动战斗时间
from utils import adb_util, game_util

game_util.load_template_images_from_directory('./image')
ip = '192.168.3.56:5555'
adb_util.connect(ip)
# 邮件任务.领取个人邮件(ip)
# 邮件任务.领取通用邮件(ip)
领取自动战斗时间.process(ip)