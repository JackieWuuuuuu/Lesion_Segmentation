import os
import shutil


def split_images(input_folder, output_folder, batch_size=400):
    # 获取输入文件夹中的所有图片文件名
    image_files = sorted(os.listdir(input_folder))

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历所有图片，按批次分组
    batch_num = 0
    for i in range(0, len(image_files), batch_size):
        # 创建新的子文件夹
        batch_folder = os.path.join(output_folder, f"batch_{batch_num:03d}")
        os.makedirs(batch_folder, exist_ok=True)

        # 将当前批次的图片复制到新的子文件夹中
        for j in range(i, min(i + batch_size, len(image_files))):
            image_file = image_files[j]
            src_path = os.path.join(input_folder, image_file)
            dst_path = os.path.join(batch_folder, image_file)
            shutil.copy(src_path, dst_path)

        batch_num += 1
        print(f"Batch {batch_num:03d} has been processed.")


# 设置输入和输出文件夹路径
input_folder = r'C:\UltraLight-VMUNet-Output\DDR_Output\4_pdr\Source_Photo'  # 替换为你图片所在的文件夹路径
output_folder = r'C:\UltraLight-VMUNet-Output\DDR_Output\4_pdr\0-399source'  # 替换为你想保存新文件夹的路径

# 调用函数进行图片分批处理
split_images(input_folder, output_folder)

