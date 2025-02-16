import cv2
from web_app import flask_app
import global_vars
import numpy as np
import os


# 加载小图的函数
def load_small_image():
    try:
        # 以二进制模式读取图片文件
        with open('./image/桌面/桌面_创建队伍.png', 'rb') as f:
            img_array = np.asarray(bytearray(f.read()), dtype=np.uint8)
        # 解码图片数据
        small_img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if small_img is None:
            print("Failed to load small image.")
        else:
            # 将加载的小图赋值给全局变量
            global_vars.small_img = small_img
            print("Small image loaded successfully.")
    except Exception as e:
        print(f"Error loading small image: {e}")


def load_small_images_from_directory(directory):
    try:
        # 检查目录是否存在
        if not os.path.exists(directory):
            print(f"Directory {directory} does not exist.")
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
                            print(f"Failed to load {filename}.")
                        else:
                            # 去掉文件扩展名，作为全局变量的键
                            var_name = os.path.splitext(filename)[0]
                            # 将加载的图片赋值给全局变量字典
                            global_vars.template_mat_map[var_name] = small_img
                            print(f"{filename} 加载成功.")
                    except Exception as e:
                        print(f"Error loading {filename}: {e}")
    except Exception as e:
        print(f"Error accessing directory: {e}")


if __name__ == '__main__':
    directory_path = './image'
    load_small_images_from_directory(directory_path)
    # 启动 Flask 应用，开启调试模式，指定端口为 8080 调试模式需要删除debug=True
    # flask_app.run(debug=True, port=8080)
    flask_app.run(port=8080)
