import os
import cv2
import numpy as np


def data_augmentation(image, mask):
    # 随机旋转
    angle = np.random.randint(-15, 15)
    image = rotate_image(image, angle)
    mask = rotate_image(mask, angle)

    # 随机缩放
    scale = np.random.uniform(0.8, 1.2)
    image = resize_image(image, scale)
    mask = resize_image(mask, scale)

    # 随机平移
    dx = np.random.randint(-30, 30)
    dy = np.random.randint(-30, 30)
    image = translate_image(image, dx, dy)
    mask = translate_image(mask, dx, dy)

    # 随机水平翻转
    if np.random.rand() > 0.5:
        image = cv2.flip(image, 1)
        mask = cv2.flip(mask, 1)

    # 随机亮度调整
    brightness = np.random.randint(-40, 40)
    image = adjust_brightness(image, brightness)

    # 随机对比度调整
    contrast = np.random.uniform(0.7, 1.3)
    image = adjust_contrast(image, contrast)

    # 随机添加高斯噪声
    if np.random.rand() > 0.5:
        image = add_gaussian_noise(image)

    # 随机高斯模糊
    if np.random.rand() > 0.5:
        image = add_gaussian_blur(image)

    # 随机裁剪
    if np.random.rand() > 0.5:
        image, mask = random_crop(image, mask)

    return image, mask


def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(image, M, (cols, rows))


def resize_image(image, scale):
    return cv2.resize(image, None, fx=scale, fy=scale)


def translate_image(image, dx, dy):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    return cv2.warpAffine(image, M, (cols, rows))


def adjust_brightness(image, brightness):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)
    h, s, v = cv2.split(hsv)
    v = np.clip(v + brightness, 0, 255).astype(np.uint8)  # Convert back to uint8
    final_hsv = cv2.merge((h.astype(np.uint8), s.astype(np.uint8), v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

def adjust_contrast(image, contrast):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB).astype(np.float32)
    l, a, b = cv2.split(lab)
    l = np.clip(contrast * l, 0, 255).astype(np.uint8)  # Adjust and clip to uint8
    updated_lab = cv2.merge((l, a.astype(np.uint8), b.astype(np.uint8)))
    return cv2.cvtColor(updated_lab, cv2.COLOR_LAB2BGR)


def add_gaussian_noise(image):
    mean = 0
    stddev = 25
    noise = np.random.normal(mean, stddev, image.shape).astype(np.float32)
    noisy_image = cv2.add(image.astype(np.float32), noise)
    return np.clip(noisy_image, 0, 255).astype(np.uint8)


def add_gaussian_blur(image):
    kernel_size = np.random.choice([3, 5, 7])
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def random_crop(image, mask):
    h, w = image.shape[:2]
    crop_size = np.random.uniform(0.7, 0.9)  # Crop to 70-90% of the original size
    crop_h, crop_w = int(h * crop_size), int(w * crop_size)

    x_start = np.random.randint(0, w - crop_w)
    y_start = np.random.randint(0, h - crop_h)

    cropped_image = image[y_start:y_start + crop_h, x_start:x_start + crop_w]
    cropped_mask = mask[y_start:y_start + crop_h, x_start:x_start + crop_w]

    return cv2.resize(cropped_image, (w, h)), cv2.resize(cropped_mask, (w, h))

# 图像和标签所在文件夹
image_folder = r'C:\VM-UNet-Data\IDRiD\1. Original Images\a. Training Set'
mask_folder = r'C:\VM-UNet-Data\IDRiD\2. All Segmentation Groundtruths\a. Training Set\MA'

# 创建保存增强图像和标签的文件夹
output_image_folder = r'C:\VM-UNet-Data\train_data\MA\images'
output_mask_folder = r'C:\VM-UNet-Data\train_data\MA\labels'
os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_mask_folder, exist_ok=True)

# 目标图像数量
target_image_count = 2000
image_count = 0

# 批量处理图像和标签
while image_count < target_image_count:
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # 读取图像和对应的标签
            image_path = os.path.join(image_folder, filename)
            mask_path = os.path.join(mask_folder, filename.replace('.jpg', '.png'))  # 假设标签使用.png格式

            image = cv2.imread(image_path)
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

            # 数据增强
            augmented_image, augmented_mask = data_augmentation(image, mask)

            # 保存增强后的图像和标签
            output_image_path = os.path.join(output_image_folder, f"{image_count}.jpg")
            output_mask_path = os.path.join(output_mask_folder, f"{image_count}.png")

            cv2.imwrite(output_image_path, augmented_image)
            cv2.imwrite(output_mask_path, augmented_mask)

            image_count += 1

            if image_count >= target_image_count:
                break

        if image_count >= target_image_count:
            break

print("批量数据增强完成！")
