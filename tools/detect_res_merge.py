import os
import shutil

# 定义源文件夹和目标文件夹
source_dirs = [f'/dev/shm/data/fire_unlabeled_res_v{i}' for i in range(1, 5)]
target_dir = '/root/autodl-tmp/fire_unlabeled_res_all'

# 创建目标文件夹及子文件夹
os.makedirs(os.path.join(target_dir, 'preds'), exist_ok=True)
os.makedirs(os.path.join(target_dir, 'vis'), exist_ok=True)


# 定义合并函数
def merge_folders(subfolder):
    for src_dir in source_dirs:
        src_path = os.path.join(src_dir, subfolder)
        for root, dirs, files in os.walk(src_path):
            for file in files:
                src_file = os.path.join(root, file)
                rel_path = os.path.relpath(root, src_path)
                dest_path = os.path.join(target_dir, subfolder, rel_path)
                os.makedirs(dest_path, exist_ok=True)
                shutil.copy2(src_file, dest_path)


# 合并 pred 和 vis 文件夹
merge_folders('preds')
merge_folders('vis')

print("文件夹合并完成！")
