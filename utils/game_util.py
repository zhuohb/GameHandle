import global_vars
from utils import adb_util
from utils import img_util
import time


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
            return item, match[0], match[1]
    return None


def find_pic_s(ip, template_name_list: list[str]):
    """
    可以查找多个图片,并且返回所有找到的图像的坐标
    :param ip:
    :param template_name_list: 模板图像列表 [图像1,图像2]
    :return: 返回所有匹配到的坐标,如
    """
    screenshot = adb_util.screenshot(ip)
    pic_info = []
    for item in template_name_list:
        match = img_util.match(screenshot, item)
        if match:
            pic_info.append((item, match[0], match[1]))
    return pic_info


# 循环匹配
def loop_match(ip, template_name):
    for i in range(10):
        pic = find_pic(ip, template_name)
        if pic:
            return pic
        else:
            time.sleep(1)
    return None


# 循环匹配
def loop_match_click(ip, template_name, width, height):
    for i in range(10):
        pic = find_pic(ip, template_name)
        if pic:
            adb_util.click(ip, pic[1], pic[2], width, height)
            return True
        else:
            time.sleep(1)
    return False


def loop_match_click_area(ip, template_name, x, y, width, height):
    for i in range(10):
        if find_pic(ip, template_name):
            adb_util.click(ip, x, y, width, height)
            return True
        else:
            time.sleep(1)
    return False


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
            final_x = pic[1] + click_area[0]
            final_y = pic[2] + click_area[1]
            adb_util.click(ip, final_x, final_y, click_area[2], click_area[3])
            return True
        else:
            adb_util.swipe(ip, 1100, 413, 500, 413, 500)
            time.sleep(1)
    print('into_fb_from_rcwf 超出循环次数')
    return False
