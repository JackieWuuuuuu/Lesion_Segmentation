import os
from PIL import Image

# 输入和输出文件夹路径
input_folder = r'C:\VM-UNet-Data\IDRiD\2. All Segmentation Groundtruths\a. Training Set\EX_withe'  # 替换为你的输入文件夹路径
output_folder = r'C:\VM-UNet-Data\IDRiD\2. All Segmentation Groundtruths\a. Training Set\EX_256'  # 替换为你的输出文件夹路径

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 定义新尺寸
new_size = (256, 256)

# 遍历文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith(".tif") or filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):  # 支持处理不同格式的文件
        # 构建完整的文件路径
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path)

        # 调整图像大小为 256×256
        img_resized = img.resize(new_size)

        # 构建输出文件路径
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)

        print(f"{filename} 调整为 {new_size} 并保存到 {output_path}")
