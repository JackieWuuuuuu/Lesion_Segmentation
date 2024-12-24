import os
import shutil
import random
from PIL import Image

# 设置文件夹路径
image_folder = r'C:\VM-UNet-Data\train_data\SE\images'  # 图像文件夹路径
label_folder = r'C:\VM-UNet-Data\train_data\SE\labels'  # 标签文件夹路径
output_train_image_folder = r'C:\VM-UNet-Data\train_data\SE\train\images'  # 训练集图像输出文件夹路径
output_train_label_folder = r'C:\VM-UNet-Data\train_data\SE\train\masks'  # 训练集标签输出文件夹路径
output_test_image_folder = r'C:\VM-UNet-Data\train_data\SE\val\images'  # 测试集图像输出文件夹路径
output_test_label_folder = r'C:\VM-UNet-Data\train_data\SE\val\masks'  # 测试集标签输出文件夹路径

# 创建输出文件夹
os.makedirs(output_train_image_folder, exist_ok=True)
os.makedirs(output_train_label_folder, exist_ok=True)
os.makedirs(output_test_image_folder, exist_ok=True)
os.makedirs(output_test_label_folder, exist_ok=True)

# 划分比例
train_ratio = 0.8  # 80% 为训练集，20% 为测试集

# 获取所有图像和标签文件
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])  # 只选择 .jpg 图像文件
label_files = sorted([f for f in os.listdir(label_folder) if f.endswith('.png')])  # 只选择 .png 标签文件

# 确保每个图像都有对应的标签
assert len(image_files) == len(label_files), "图像文件和标签文件数量不匹配！"

# 随机打乱图像文件列表
random.shuffle(image_files)

# 计算划分索引
split_index = int(len(image_files) * train_ratio)

# 划分训练集和测试集
train_image_files = image_files[:split_index]
test_image_files = image_files[split_index:]

# 处理图像并保存为 256x256 png 格式
def resize_image(image_path, size=(256, 256)):
    with Image.open(image_path) as img:
        img_resized = img.resize(size, Image.LANCZOS)
        return img_resized

# 复制图像和标签到训练集
for image_name in train_image_files:
    label_name = image_name.replace('.jpg', '.png')  # 对应的标签文件名
    image_path = os.path.join(image_folder, image_name)
    label_path = os.path.join(label_folder, label_name)

    # 目标路径
    train_image_path = os.path.join(output_train_image_folder, image_name.replace('.jpg', '.png'))  # 输出为 PNG 格式
    train_label_path = os.path.join(output_train_label_folder, label_name)

    # 复制和调整图像大小
    resized_image = resize_image(image_path)  # 调整并获取图像
    resized_image.save(train_image_path, 'PNG')  # 保存为 256x256 PNG 格式

    # 复制和调整标签大小
    resized_label = resize_image(label_path)  # 调整并获取标签
    resized_label.save(train_label_path, 'PNG')  # 保存为 256x256 PNG 格式

# 复制图像和标签到测试集
for image_name in test_image_files:
    label_name = image_name.replace('.jpg', '.png')  # 对应的标签文件名
    image_path = os.path.join(image_folder, image_name)
    label_path = os.path.join(label_folder, label_name)

    # 目标路径
    test_image_path = os.path.join(output_test_image_folder, image_name.replace('.jpg', '.png'))  # 输出为 PNG 格式
    test_label_path = os.path.join(output_test_label_folder, label_name)

    # 复制和调整图像大小
    resized_image = resize_image(image_path)  # 调整并获取图像
    resized_image.save(test_image_path, 'PNG')  # 保存为 256x256 PNG 格式

    # 复制和调整标签大小
    resized_label = resize_image(label_path)  # 调整并获取标签
    resized_label.save(test_label_path, 'PNG')  # 保存为 256x256 PNG 格式

print("图像和标签数据划分完成，所有图像和标签已调整为 256x256，并保存为 PNG 格式。")
