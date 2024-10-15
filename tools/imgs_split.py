import os
import shutil

from math import ceil


def split_images_into_four_folders(source_folder, target_base_folder):
    # 获取源文件夹中所有的 JPG 图片文件
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]

    # 计算每个目标文件夹中应包含的图片数量
    total_images = len(image_files)
    images_per_folder = ceil(total_images / 4)

    # 对图片列表进行排序（可选），确保分配的一致性
    image_files.sort()

    # 创建四个目标文件夹并分配图片
    for i in range(1, 5):
        target_folder = os.path.join(target_base_folder, f'folder_{i}')
        os.makedirs(target_folder, exist_ok=True)

        # 计算当前分割的起止索引
        start_idx = (i - 1) * images_per_folder
        end_idx = i * images_per_folder
        images_to_copy = image_files[start_idx:end_idx]

        # 将图片复制到目标文件夹
        for image_file in images_to_copy:
            src_path = os.path.join(source_folder, image_file)
            dst_path = os.path.join(target_folder, image_file)
            shutil.copy2(src_path, dst_path)

        print(f"已将 {len(images_to_copy)} 张图片复制到 {target_folder}")


# 使用示例：
# 请替换 'path_to_source_folder' 和 'path_to_target_base_folder'
# split_images_into_four_folders('path_to_source_folder', 'path_to_target_base_folder')


if __name__ == "__main__":
    source_folder = "/dev/shm/data/fire_unlabeled/VOCdevkit/VOC2007/JPEGImages/"  # 替换为您的源图片文件夹路径
    target_base_folder = "/dev/shm/data/split"  # 替换为您的目标文件夹根路径
    split_images_into_four_folders(source_folder, target_base_folder)
