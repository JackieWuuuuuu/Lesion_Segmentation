import os
import numpy as np
from PIL import Image


def images_to_npy(image_folder, output_npy_file):
    images = []
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # 修改文件扩展名
            img_path = os.path.join(image_folder, filename)
            img = Image.open(img_path).convert('RGB')  # 将图片转换为RGB格式
            img_array = np.array(img)
            images.append(img_array)

    # 将图片数组转换为numpy数组
    images_array = np.array(images)
    # 保存为.npy文件
    np.save(output_npy_file, images_array)
    print(f'Saved {len(images)} images to {output_npy_file}')


# 使用示例
image_folder = r'C:\xxx\xxx\xxx'  # 替换图片文件夹路径
output_npy_file = r'C:\xxx\xxx\xxx.npy'
images_to_npy(image_folder, output_npy_file)
