from task import 材料副本
from utils import adb_util
import start



if __name__ == '__main__':
    directory_path = './image'
    start.load_small_images_from_directory(directory_path)
    adb_util.connect('192.168.1.70:5555')
    材料副本.process('192.168.1.70:5555')