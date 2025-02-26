import time

import cv2
import numpy as np

import global_vars
from utils import img_util, game_util


def match(large_img, small_img, threshold=0.98, debug=True):
    """
    模板匹配,返回第一个坐标
    :param large_img: 大图,这里指的是截图
    :param small_img: 小图,这里指的是模板图像
    :param threshold: 相似度阈值,最大为1
    :param debug: 调试开关，开启会保存截图
    :return: 返回匹配到的第一个坐标,如 (10,10)
    """
    print('调用一次')
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


def process1():
    # 读取图片
    image = cv2.imread('task/xx.png')

    # 检查图片是否成功读取
    if image is None:
        print("Error: Could not read the image.")
        exit()

    # 获取图片的高度和宽度
    height, width = image.shape[:2]

    # 生成横线的x坐标列表
    x_coords = [64 + 66 * e for e in range(13)]

    # 生成竖线的y坐标列表
    y_coords = [78 + 66 * e for e in range(13)]

    # 创建一个空的矩阵，大小为13x10，每个元素存储x和y坐标
    matrix = np.zeros((13, 10, 2), dtype=int)  # 每个元素存储x和y坐标

    # 填充矩阵
    for i in range(13):
        for j in range(10):
            x = x_coords[i]
            y = y_coords[j]
            # 检查坐标是否在图片范围内
            if 0 <= x < width and 0 <= y < height:
                matrix[i, j] = (x, y)
            else:
                matrix[i, j] = (-1, -1)  # 表示超出范围

    # 打印矩阵
    print("矩阵维度:", matrix.shape)
    print("矩阵内容:")
    for i in range(13):
        for j in range(10):
            print(f"矩阵[{i}][{j}]: {matrix[i, j]}")

    # 画横线
    cv2.line(image, (64, 0), (64, height), (0, 0, 255), 1)
    for e in range(1, 13):
        # cv2.line(image, (64 + 66 * e, 0), (64 + 66 * e, height), (0, 0, 255), 1)
        cv2.line(image, (64 + 66 * e - 15, 0), (64 + 66 * e - 15, height), (0, 0, 255), 1)
        cv2.line(image, (64 + 66 * e + 15, 0), (64 + 66 * e + 15, height), (0, 0, 255), 1)

    # 画竖线
    cv2.line(image, (0, 78), (width, 78), (0, 0, 255), 1)
    for e in range(1, 10):
        cv2.line(image, (0, 78 + 66 * e - 15), (width, 78 + 66 * e - 15), (0, 0, 255), 1)
        cv2.line(image, (0, 78 + 66 * e + 15), (width, 78 + 66 * e + 15), (0, 0, 255), 1)

    # 保存图片
    cv2.imwrite('image_with_line.jpg', image)


def get_coordinate_matrix():
    # 读取图片
    image = cv2.imread('task/xx.png')
    # 检查图片是否成功读取
    if image is None:
        print("Error: Could not read the image.")
        exit()
    # 获取图片的高度和宽度
    height, width = image.shape[:2]
    # 生成横线的x坐标列表
    x_coords = [64 + 66 * e for e in range(13)]
    # 生成竖线的y坐标列表
    y_coords = [78 + 66 * e for e in range(13)]
    # 创建一个空的矩阵，大小为13x10，每个元素存储x和y坐标
    matrix = np.zeros((13, 10, 2), dtype=int)  # 每个元素存储x和y坐标
    # 填充矩阵
    for i in range(13):
        for j in range(10):
            x = x_coords[i]
            y = y_coords[j]
            # 检查坐标是否在图片范围内
            if 0 <= x < width and 0 <= y < height:
                matrix[i, j] = (x, y)
            else:
                matrix[i, j] = (-1, -1)  # 表示超出范围
    return matrix


def fill_number_matrix(coordinate_matrix, match_coordinate_list, number_matrix, number):
    # 遍历坐标矩阵
    for i in range(13):
        for j in range(10):
            x, y = coordinate_matrix[i][j]
            # 检查是否在任何一个矩形中
            for rect in match_coordinate_list:
                rect_x, rect_y = rect
                if rect_x <= x <= rect_x + 30 and rect_y <= y <= rect_y + 30:
                    number_matrix[i][j] = number
                    break  # 停止检查其他矩形


if __name__ == '__main__':
    # 加载模板图像
    game_util.load_template_images_from_directory('./image')
    # process1()

    # 获取坐标矩阵
    coordinate_matrix = get_coordinate_matrix()

    # 初始化结果矩阵
    result_matrix = [[-1 for _ in range(10)] for _ in range(13)]
    number_list = ['矩阵数字1', '矩阵数字2', '矩阵数字3', '矩阵数字4', '矩阵数字5', '矩阵数字6', '矩阵数字7', '矩阵数字8']
    for index, main_e in enumerate(number_list):
        result = match(cv2.imread('task/xx.png'), main_e)
        fill_number_matrix(coordinate_matrix, result, result_matrix, index + 1)

    print(f'结果矩阵: {result_matrix}')
