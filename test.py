from task import 材料副本, 精英副本
from utils import adb_util, game_util
import start

if __name__ == '__main__':
    ip = '192.168.1.70:5555'
    directory_path = './image'
    start.load_small_images_from_directory(directory_path)
    adb_util.connect(ip)
    if game_util.into_desktop(ip):
        # 材料副本.process(ip)
        精英副本.process(ip)
