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


# 模板匹配,返回坐标
def match(large_img, small_img, threshold=0.9, debug=True):
    if small_img is not None:
        # 执行模板匹配
        result = cv2.matchTemplate(large_img, global_vars.template_mat_map[small_img], cv2.TM_CCOEFF_NORMED)
        # 找到所有匹配得分大于阈值的位置
        locations = np.where(result >= threshold)
        h, w, _ = global_vars.template_mat_map[small_img].shape

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
            for loc in zip(*locations[::-1]):
                top_left = loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv2.rectangle(large_img, top_left, bottom_right, (0, 255, 0), 2)
                output_path = f'debug/output{time.strftime("%Y%m%d%H%M%S", time.localtime())}.jpg'
                cv2.imwrite(output_path, large_img)

        return coordinates
    else:
        return None
