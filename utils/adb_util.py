import random
import subprocess
import time

import cv2
import numpy as np

from decorator.retry_decorator import retry


def connect(ip):
    return subprocess.run(['adb', 'connect', ip], capture_output=True, text=True)


def adb_fail(ip, *args, **kwargs):
    print(f"执行自定义函数，参数: ip={ip}, args={args}, kwargs={kwargs}")
    connect(ip)


@retry(max_retries=3, delay=2, custom_func=adb_fail)
def click(ip, x, y, width, height):
    try:
        # 在指定矩形区域内随机生成点击的 x 和 y 坐标
        random_x = random.randint(x, x + width - 1)
        random_y = random.randint(y, y + height - 1)
        print(f'点击坐标: {random_x},{random_y}')
        command = ['adb', '-s', ip, 'shell', 'input', 'tap', str(random_x), str(random_y)]
        subprocess.run(command, capture_output=True, text=True, check=True)
        # 暂停一下
        time.sleep(random.uniform(0.7, 1.2))
        return True
    except subprocess.CalledProcessError as e:
        print(f"执行 ADB 点击命令时出错: {e.stderr}")
        return False


@retry(max_retries=3, delay=2, custom_func=adb_fail)
def swipe(ip, x1, y1, x2, y2, duration):
    try:
        command = ['adb', '-s', ip, 'shell', 'input', 'swipe', str(x1), str(y1), str(x2), str(y2), str(duration)]
        subprocess.run(command, capture_output=True, text=True, check=True)
        time.sleep(random.uniform(1, 1.5))
        return True
    except subprocess.CalledProcessError as e:
        print(f"执行 swipe 命令时出错: {e.stderr}")
        return False


@retry(max_retries=3, delay=2, custom_func=adb_fail)
def screenshot(ip):
    try:
        command = ['adb', '-s', ip, 'exec-out', 'screencap', '-p']
        result = subprocess.run(command, capture_output=True, check=True)
        img_bytes = result.stdout
        # 将字节数据转换为 numpy 数组
        img_array = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        print(f"解码图像时出错: {e}")
        return None
