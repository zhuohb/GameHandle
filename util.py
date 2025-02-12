import cv2
import base64


# 封装模板匹配逻辑的函数
def perform_template_matching(large_img, small_img):
    if small_img is not None:
        result = cv2.matchTemplate(large_img, small_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        h, w, _ = small_img.shape
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
