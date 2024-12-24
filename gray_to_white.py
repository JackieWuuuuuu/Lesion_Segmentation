import os
from PIL import Image

# 输入和输出文件夹路径
input_folder = r'C:\VM-UNet-Data\IDRiD\2. All Segmentation Groundtruths\a. Training Set\EX_gray'  # 替换为你的输入文件夹路径
output_folder = r'C:\VM-UNet-Data\IDRiD\2. All Segmentation Groundtruths\a. Training Set\EX_withe'  # 替换为你的输出文件夹路径

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 定义颜色范围，灰色的范围
gray_lower = (47, 79, 79)  # 最低灰色值
gray_upper = (220, 220, 220)  # 最高灰色值

# 遍历文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith(".tif") or filename.endswith(".png"):  # 支持处理 .tif 或 .png 文件
        # 构建完整的文件路径
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path)
        img = img.convert("RGB")  # 转换为RGB模式

        # 获取图像的像素数据
        pixels = img.load()

        # 遍历图像的每个像素
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]

                # 检查像素是否在灰色范围内
                if gray_lower <= (r, g, b) <= gray_upper:
                    # 将灰色像素转换为白色
                    pixels[i, j] = (255, 255, 255)

        # 构建输出文件路径
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

        print(f"{filename} 修改完成，保存到 {output_path}")
