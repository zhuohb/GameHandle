# start.py
import cv2
from web_app import flask_app
import global_vars


# 加载小图的函数
def load_small_image():
    try:
        # 读取小图文件，这里假设小图名为 small.jpg，可按需修改
        small_img = cv2.imread('small.png', cv2.IMREAD_COLOR)
        if small_img is None:
            print("Failed to load small image.")
        else:
            # 将加载的小图赋值给全局变量
            global_vars.small_img = small_img
            print("Small image loaded successfully.")
    except Exception as e:
        print(f"Error loading small image: {e}")


if __name__ == '__main__':
    # 在应用启动时加载小图
    load_small_image()
    # 启动 Flask 应用，开启调试模式，指定端口为 8080
    flask_app.run(debug=True, port=8080)
