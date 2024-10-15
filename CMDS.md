# train

screen bash ./tools/dist_train.sh \
    projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_90k_coco-s1-p10.py \
    7

screen bash ./tools/dist_train.sh \
    projects/MixPL/configs/mixpl_dino-4scale_swin_l_fpn_90k_coco-s1-p10.py \
    2

python tools/train.py projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_90k_coco-s1-p10.py

screen bash ./tools/dist_train.sh \
    projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_fire.py \
    7

# infer

export PYTHONPATH=$PYTHONPATH:$(pwd)

python demo/image_demo.py /dev/shm/data/split/folder_1/ \
    projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_fire.py \
    --weights work_dirs/mixpl_dino-4scale_r50_fpn_fire/iter_90000.pth \
    --device cuda:0 \
    --out-dir /dev/shm/data/fire_unlabeled_res_v1

python demo/image_demo.py /dev/shm/data/split/folder_2/ \
    projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_fire.py \
    --weights work_dirs/mixpl_dino-4scale_r50_fpn_fire/iter_90000.pth \
    --device cuda:1 \
    --out-dir /dev/shm/data/fire_unlabeled_res_v2

python demo/image_demo.py /dev/shm/data/split/folder_3/ \
    projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_fire.py \
    --weights work_dirs/mixpl_dino-4scale_r50_fpn_fire/iter_90000.pth \
    --device cuda:0 \
    --out-dir /dev/shm/data/fire_unlabeled_res_v3

python demo/image_demo.py /dev/shm/data/split/folder_4/ \
    projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_fire.py \
    --weights work_dirs/mixpl_dino-4scale_r50_fpn_fire/iter_90000.pth \
    --device cuda:1 \
    --out-dir /dev/shm/data/fire_unlabeled_res_v4

# data

ln -s /dev/shm/data/ ./
ln -s ~/autodl-tmp/ckpts ./ckpt
ln -s ~/autodl-tmp/mixpl_dino-4scale_r50_fpn_fire ./work_dirs

# web

https://huggingface.co/czm369/MixPL
