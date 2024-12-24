import os
from PIL import Image

# 输入和输出文件夹路径
input_folder = r'C:\VM-UNet-Data\IDRiD\2. All Segmentation Groundtruths\a. Training Set\4. Soft Exudates'  # 替换为你的.tif文件夹路径
output_folder = r'C:\VM-UNet-Data\IDRiD\2. All Segmentation Groundtruths\a. Training Set\SE'  # 替换为输出的白色PNG文件夹路径

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有.tif文件
for filename in os.listdir(input_folder):
    if filename.endswith(".tif"):
        # 构建完整的文件路径
        tif_path = os.path.join(input_folder, filename)

        # 打开 .tif 文件
        img = Image.open(tif_path)

        # 转换为 RGB 模式
        img_rgb = img.convert("RGB")
        pixels = img_rgb.load()

        # 遍历图像的每个像素
        for i in range(img_rgb.size[0]):
            for j in range(img_rgb.size[1]):
                r, g, b = pixels[i, j]

                # 只针对红色部分进行处理
                # 判断红色通道是否大于一定阈值（即识别红色部分）
                if r > 100 and g < 80 and b < 80:  # 红色部分的阈值可以根据实际情况调整
                    # 将红色部分转换为白色
                    pixels[i, j] = (255, 255, 255)

        # 去掉文件名中的 "_EX" 后缀并保存为 .png 格式
        new_filename = filename.replace('_SE', '').replace('.tif', '.png')
        output_path = os.path.join(output_folder, new_filename)

        # 保存修改后的图像
        img_rgb.save(output_path)

        print(f"{filename} 转换并修改为白色 PNG，保存到 {output_path}")

print("批量转换完成！")
