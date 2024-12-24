import os

def delete_superpixels_images(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件名是否以_superpixels结尾
        if filename.endswith('_superpixels.png') or filename.endswith('_superpixels.jpg'):
            # 构建完整文件路径
            file_path = os.path.join(folder_path, filename)
            # 删除文件
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# 替换为你的图片文件夹路径
folder_path = r"C:\baidunetdiskdownload\ISIC-2017_Training_Data\ISIC-2017_Training_Data"
delete_superpixels_images(folder_path)
