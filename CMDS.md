# train

bash ./tools/dist_train.sh \
    projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_90k_coco-s1-p10.py \
    2

python tools/train.py projects/MixPL/configs/mixpl_dino-4scale_r50_fpn_90k_coco-s1-p10.py


# data

ln -s /dev/shm/data/ ./
ln -s ~/autodl-tmp/ckpts ./ckpt