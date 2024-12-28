import cv2
import numpy as np
import os

# 定义输入文件夹和输出文件夹
folders = [r'C:\UltraLight-VMUNet-Output\DDR_Output\4_pdr\EX_Output',
           r'C:\UltraLight-VMUNet-Output\DDR_Output\4_pdr\H_Output',
           r'C:\UltraLight-VMUNet-Output\DDR_Output\4_pdr\MA_Output',
           r'C:\UltraLight-VMUNet-Output\DDR_Output\4_pdr\SE_Output']
output_folder = r'C:\UltraLight-VMUNet-Output\DDR_Output\4_pdr\Combine'
os.makedirs(output_folder, exist_ok=True)  # 创建输出文件夹

# 定义颜色范围
color_ranges = [
    ([0, 100, 100], [10, 255, 255]),   # 红色
    ([100, 100, 100], [140, 255, 255]), # 蓝色
    ([40, 100, 100], [80, 255, 255]),   # 绿色
    ([150, 50, 50], [180, 255, 255])  # 粉色
]

# 获取所有文件名
image_names = os.listdir(folders[0])  # 假设所有文件夹中的图片同名

for image_name in image_names:
    if image_name.endswith('.jpg') or image_name.endswith('.png'):
        result = None  # 初始化结果图像

        # 处理每个文件夹中的同名图片
        for i, folder in enumerate(folders):
            img_path = os.path.join(folder, image_name)
            if os.path.exists(img_path):  # 检查文件是否存在
                img = cv2.imread(img_path)

                # 提取颜色
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, np.array(color_ranges[i][0]), np.array(color_ranges[i][1]))
                colored_part = cv2.bitwise_and(img, img, mask=mask)

                # 初始化结果图像
                if result is None:
                    result = np.zeros_like(img)  # 创建一个与原图像大小相同的空白图像

                # 将提取的颜色区域覆盖到空白图像上
                result = cv2.add(result, colored_part)

        # 保存拼接后的图像到输出文件夹
        output_path = os.path.join(output_folder, image_name)
        cv2.imwrite(output_path, result)

