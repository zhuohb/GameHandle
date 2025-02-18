import os
import time

import cv2
import numpy as np

import global_vars
from utils import adb_util
from utils import img_util


def load_template_images_from_directory(directory):
    """
    从目录加载模板图像
    加载进内存减少资源消耗
    :param directory: 模板图像所在的目录,基于项目的相对地址
    :return:
    """
    try:
        # 检查目录是否存在
        if not os.path.exists(directory):
            print(f"目录 {directory} 不存在.")
            return

        # 使用 os.walk 递归遍历目录及其子目录
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith('.png'):
                    file_path = os.path.join(root, filename)
                    try:
                        # 以二进制模式读取图片文件
                        with open(file_path, 'rb') as f:
                            img_array = np.asarray(bytearray(f.read()), dtype=np.uint8)
                        # 解码图片数据
                        small_img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        if small_img is None:
                            print(f"加载失败 {filename}.")
                        else:
                            # 去掉文件扩展名，作为全局变量的键
                            var_name = os.path.splitext(filename)[0]
                            # 先检查是否重名
                            if var_name in global_vars.template_mat_map:
                                print(f'模板图像重名:{var_name}')
                            else:
                                # 将加载的图片赋值给全局变量字典
                                global_vars.template_mat_map[var_name] = small_img
                                print(f"加载成功 {filename}")
                    except Exception as e:
                        print(f"加载时出错 {filename}: {e}")
    except Exception as e:
        print(f"访问目录时出错: {e}")


def find_pic(ip, template_name: str | list[str]):
    """
    可以查找多个图片,只返回第一个找到的X Y坐标
    :param ip:
    :param template_name:
    :return:
    """
    # 如果是字符串,就转为列表方便匹配
    if isinstance(template_name, str):
        template_name = [template_name]
    # 截图
    screenshot = adb_util.screenshot(ip)
    # 循环匹配,返回第一个匹配到的坐标
    for item in template_name:
        match = img_util.match(screenshot, item)
        if match:
            return {item: (match[0], match[1])}
    return None


def find_pic_s(ip, template_name_list: list[str], debug=True):
    """
    可以查找多个图片,并且返回所有找到的图像的坐标
    :param debug:
    :param ip:
    :param template_name_list: 模板图像列表 [图像1,图像2]
    :return: 返回所有匹配到的坐标,如
    """
    screenshot = adb_util.screenshot(ip)
    pic_info = {}
    for item in template_name_list:
        match = img_util.match(screenshot, item)
        if match:
            pic_info[item] = (match[0], match[1])
    return pic_info


# 循环匹配
def loop_match(ip, template_name):
    for i in range(20):
        pic = find_pic(ip, template_name)
        if pic:
            return pic
        else:
            time.sleep(1)
    return None


# 循环匹配
def loop_match_click(ip, template_name, width, height):
    for i in range(20):
        pic = find_pic(ip, template_name)
        if pic:
            adb_util.click(ip, pic[template_name][0], pic[template_name][1], width, height)
            return True
        else:
            time.sleep(1)
    return False


def loop_match_click_area(ip, template_name, x, y, width, height):
    for i in range(20):
        if find_pic(ip, template_name):
            adb_util.click(ip, x, y, width, height)
            return True
        else:
            time.sleep(1)
    return False


def close_all(ip):
    """
    关闭所有窗口
    :param ip:
    :return:
    """
    temp_list = [global_vars.模板_关闭_菜单, global_vars.模板_关闭_日常玩法]
    for e in range(5):
        pic_info = find_pic_s(ip, temp_list)
        pic = None
        if global_vars.模板_关闭_日常玩法 in pic_info:
            pic = pic_info[global_vars.模板_关闭_日常玩法]
        elif global_vars.模板_关闭_菜单 in pic_info:
            pic = pic_info[global_vars.模板_关闭_菜单]
        else:
            print('未检测到关闭按钮')
            time.sleep(0.2)
        if pic:
            adb_util.click(ip, pic[0], pic[1], 20, 20)


# 从桌面进入日常玩法
def into_rcwf_from_desktop(ip):
    if not loop_match_click_area(ip, global_vars.模板_桌面_创建队伍, *global_vars.坐标_菜单):
        print('into_rcwf_from_desktop 步骤1失败')
        return False
    if not loop_match_click_area(ip, global_vars.模板_菜单_个人主页, *global_vars.坐标_菜单_日常玩法):
        print('into_rcwf_from_desktop 步骤2失败')
        return False
    if not loop_match(ip, global_vars.模板_副本通用_日常玩法_主页):
        print('into_rcwf_from_desktop 步骤3失败')
        return False
    return True


# 从日常玩法列表进入对应副本
def into_fb_from_rcwf(ip, template_name, click_area):
    for i in range(10):
        pic = find_pic(ip, template_name)
        if pic:
            # 计算偏移
            final_x = pic[template_name][0] + click_area[0]
            final_y = pic[template_name][1] + click_area[1]
            adb_util.click(ip, final_x, final_y, click_area[2], click_area[3])
            return True
        else:
            adb_util.swipe(ip, 1100, 413, 500, 413, 500)
            time.sleep(1)
    print('into_fb_from_rcwf 超出循环次数')
    return False


def into_desktop(ip):
    """
    检测广告等,进入桌面
    :param ip:
    :return:
    """
    temp_list = [global_vars.模板_广告_前往商店, global_vars.模板_广告_快乐成长派对, global_vars.模板_广告_日程管理,
                 global_vars.模板_广告_王中王争霸战, global_vars.模板_广告_首充福利, global_vars.模板_广告_25元,
                 global_vars.模板_桌面_创建队伍]
    for i in range(10):
        pic_info = find_pic_s(ip, temp_list)
        if global_vars.模板_广告_前往商店 in pic_info or global_vars.模板_广告_首充福利 in pic_info or global_vars.模板_广告_25元 in pic_info:
            adb_util.click(ip, 1115, 31, 35, 35)
        elif global_vars.模板_广告_日程管理 in pic_info:
            adb_util.click(ip, 47, 667, 20, 20)
            adb_util.click(ip, 1212, 54, 20, 20)
        elif global_vars.模板_广告_快乐成长派对 in pic_info:
            adb_util.click(ip, 135, 618, 20, 20)
            adb_util.click(ip, 1136, 56, 25, 25)
        elif global_vars.模板_广告_王中王争霸战 in pic_info:
            adb_util.click(ip, 1040, 86, 30, 30)
        elif global_vars.模板_桌面_创建队伍 in pic_info:
            return True
        else:
            # 没有其他情况,尝试点击组队按钮
            adb_util.click(ip, 14, 254, 20, 18)
    print('into_desktop 超出循环次数')
    return False


def calculate_role_page(current_role_index, role_per_page_count):
    """
    当前角色所在的页码

    :param current_role_index: 当前角色的索引（从 1 开始）
    :param role_per_page_count: 每页固定的角色数量
    :return: 当前角色所在的页码（从 1 开始）
    """
    return (current_role_index - 1) // role_per_page_count + 1


def calculate_current_role_in_current_page_index(current_role_index, role_per_page_count):
    """
    计算当前角色在当前页的索引

    :param current_role_index: 当前角色的索引（从 1 开始）
    :param role_per_page_count: 每页固定的角色数量
    :return: 当前角色在当前页的索引（从 1 开始）
    """
    return ((current_role_index - 1) % role_per_page_count) + 1
