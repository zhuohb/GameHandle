import cv2
import base64
import numpy as np
import global_vars
import time


# 模板匹配,在图上画框,返回图像 适用于web
def web_match(large_img, small_img, threshold=0.9):
    if small_img is not None:
        # 执行模板匹配
        result = cv2.matchTemplate(large_img, small_img, cv2.TM_CCOEFF_NORMED)
        # 找到所有匹配得分大于阈值的位置
        locations = np.where(result >= threshold)
        h, w, _ = small_img.shape

        # 在大图像上绘制所有匹配的矩形框
        for loc in zip(*locations[::-1]):
            top_left = loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(large_img, top_left, bottom_right, (0, 255, 0), 2)

        # 将图像编码为 PNG 格式的字节流
        _, buffer = cv2.imencode('.png', large_img)
        img_bytes = buffer.tobytes()
        # 将字节流进行 Base64 编码
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        output_image = f'data:image/png;base64,{img_base64}'
        return output_image
    else:
        return None


def match(large_img, small_img, threshold=0.9, debug=False):
    """
    模板匹配,返回第一个坐标
    :param large_img: 大图,这里指的是截图
    :param small_img: 小图,这里指的是模板图像
    :param threshold: 相似度阈值,最大为1
    :param debug: 调试开关，开启会保存截图
    :return: 返回匹配到的所有坐标,如 [(10,10),(10,10)]
    """
    if small_img is not None:
        small_img_mat = global_vars.template_mat_map[small_img]
        # 执行模板匹配
        result = cv2.matchTemplate(large_img, small_img_mat, cv2.TM_CCOEFF_NORMED)
        # 找到所有匹配得分大于阈值的位置
        locations = np.where(result >= threshold)
        h, w, _ = small_img_mat.shape

        coordinates = []
        # 遍历所有匹配位置，收集坐标
        for loc in zip(*locations[::-1]):
            # 左上角
            top_left = loc
            # 右下角 暂时不用
            bottom_right = (top_left[0] + w, top_left[1] + h)
            coordinates.append(top_left)

        if debug:
            # 在大图像上绘制所有匹配的矩形框
            for top_left in coordinates:
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv2.rectangle(large_img, top_left, bottom_right, (0, 255, 0), 1)
            output_path = f'debug/output{time.strftime("%Y%m%d%H%M%S", time.localtime())}.jpg'
            cv2.imwrite(output_path, large_img)
        if coordinates:
            return coordinates
    # 没有匹配到 就返回空
    return None
