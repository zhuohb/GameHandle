from task import 全局任务
from utils import adb_util, game_util

game_util.load_template_images_from_directory('./image')
ip = '192.168.3.56:5555'
adb_util.connect(ip)
全局任务.领取通用邮件(ip)
