import cv2


def bmp_to_png(bmp_path, png_path):
    # 读取BMP图像
    image = cv2.imread(bmp_path)

    if image is not None:
        # 保存为PNG图像
        cv2.imwrite(png_path, image)
        print(f"成功将 {bmp_path} 转换为 {png_path}")
    else:
        print(f"无法读取 {bmp_path} 图像，请检查文件路径或文件格式是否正确。")


# 指定BMP图像的路径
# bmp_file = '1.bmp'
# 指定要保存的PNG图像的路径
# png_file = '2.png'

# 调用函数进行转换
for e in range(1, 9):
    bmp_to_png(f'{e}.bmp', f'矩阵数字{e}.png')
