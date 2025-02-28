import time

import cv2
import numpy as np

import global_vars
from utils import img_util, game_util, adb_util


def test():
    # 读取图片
    image = cv2.imread('xx.png')
    # 检查图片是否成功读取
    if image is None:
        print("错误：无法读取图像。")
        exit()
    # 获取图片的高度和宽度
    height, width = image.shape[:2]
    # 画竖线
    cv2.line(image, (64, 0), (64, height), (0, 0, 255), 1)
    for e in range(1, 13):
        cv2.line(image, (64 + 66 * e, 0), (64 + 66 * e, height), (0, 0, 255), 1)

    # 画横线
    cv2.line(image, (0, 78), (width, 78), (0, 0, 255), 1)
    for e in range(1, 10):
        cv2.line(image, (0, 78 + 66 * e), (width, 78 + 66 * e), (0, 0, 255), 1)
    # 保存图片
    cv2.imwrite('image_with_line.jpg', image)


# 获取坐标矩阵,也就是截图中每个数字的中心坐标
def get_coordinate_matrix():
    # 生成x和y坐标列表，分别对应10个和13个元素
    # [64, 130, 196, 262, 328, 394, 460, 526, 592, 658, 724, 790, 856]
    x_coords = [64 + 66 * e for e in range(13)]
    # [78, 144, 210, 276, 342, 408, 474, 540, 606, 672]
    y_coords = [78 + 66 * e for e in range(10)]

    # 创建一个空的矩阵，大小为10x13，每个元素存储x和y坐标
    matrix = np.zeros((10, 13, 2), dtype=int)

    # 填充矩阵
    for i in range(10):
        for j in range(13):
            x = x_coords[j]
            y = y_coords[i]
            # 检查坐标是否在图片范围内
            if 0 <= x < 1280 and 0 <= y < 720:
                matrix[i, j] = (x, y)
            else:
                # 表示超出范围
                matrix[i, j] = (-1, -1)
    return matrix


# 遍历坐标矩阵
def fill_number_matrix(coordinate_matrix, match_coordinate_list, number_matrix, number):
    for i in range(10):
        for j in range(13):
            x, y = coordinate_matrix[i][j]
            # 检查是否在任何一个矩形中
            for rect in match_coordinate_list:
                rect_x, rect_y = rect
                if rect_x <= x <= rect_x + 30 and rect_y <= y <= rect_y + 30:
                    number_matrix[i][j] = number
                    # 停止检查其他矩形
                    break


def process(screenshot):
    # 获取坐标矩阵
    coordinate_matrix = get_coordinate_matrix()
    # 初始化结果矩阵
    result_matrix = [[-1 for _ in range(13)] for _ in range(10)]
    number_list = ['矩阵数字1', '矩阵数字2', '矩阵数字3', '矩阵数字4', '矩阵数字5', '矩阵数字6', '矩阵数字7', '矩阵数字8']
    for index, main_e in enumerate(number_list):
        # result = img_util.match(cv2.imread('xx.png'), main_e, threshold=0.99)
        result = img_util.match(screenshot, main_e, threshold=0.99)
        fill_number_matrix(coordinate_matrix, result, result_matrix, index + 1)

    print(f'结果矩阵: {result_matrix}')
    return result_matrix



# 深度优先搜索列出组合
def dfs(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = []

    def dfs(i, j, current_sum, path, visited):
        if current_sum == 10:
            result.append(path.copy())
            return
        if current_sum > 10 or len(path) >= 4:
            return
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x = i + dx
            y = j + dy
            if 0 <= x < rows and 0 <= y < cols and not visited[x][y]:
                visited[x][y] = True
                new_sum = current_sum + matrix[x][y]
                new_path = path + [(x, y)]
                dfs(x, y, new_sum, new_path, visited.copy())
                # 重复使用当前数字
                # visited[x][y] = False

    for i in range(rows):
        for j in range(cols):
            visited[i][j] = True
            dfs(i, j, matrix[i][j], [(i, j)], visited.copy())
            # 重复使用当前数字
            # visited[i][j] = False
    return result

if __name__ == '__main__':
    game_util.load_template_images_from_directory('../image')
    ip = '192.168.1.134:5555'
    adb_util.connect(ip)
    screenshot = adb_util.screenshot(ip)
    l = process(screenshot)
    dfs1 = dfs(l)
    print(dfs1)
