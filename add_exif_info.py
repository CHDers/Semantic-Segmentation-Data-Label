# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/4 11:18
# @Author  : Yanjun Hao
# @Site    : 
# @File    : add_exif_info.py
# @Software: PyCharm 
# @Comment :

# https://blogs.boycechen.cn/p/da16c9e5.html

import piexif
import glob
import os
from PIL import Image
from rich import print
from tqdm import tqdm


def add_exif_info(src_img_path, dst_img_path) -> None:
    # 将照片实例化
    exif_info = piexif.load(src_img_path)
    # 将以上修改的数据，加载二进制数据
    exif_bytes = piexif.dump(exif_info)
    # 将照片实例化
    img = Image.open(dst_img_path)
    # 将exif信息写入图片
    img.save(dst_img_path, exif=exif_bytes)


def main(src_folder_path, dst_folder_path):
    src_image_files = glob.glob(os.path.join(src_folder_path, '*.[pj]*[ng]*'))  # 匹配所有图片格式的文件
    dst_image_files = glob.glob(os.path.join(dst_folder_path, '*.[pj]*[ng]*'))  # 匹配所有图片格式的文件

    # 按照文件名排序
    sorted_src_images = list(sorted(src_image_files))
    sorted_dst_images = list(sorted(dst_image_files))

    assert len(sorted_src_images) == len(
        sorted_dst_images), "The number of source images and destination images are not equal."

    assert all(
        os.path.splitext(os.path.basename(src_img_path))[0] == os.path.splitext(os.path.basename(dst_img_path))[0] for
        src_img_path, dst_img_path in
        zip(sorted_src_images,
            sorted_dst_images)), "The filenames of source images and destination images do not match."

    for img_path1, img_path2 in tqdm(zip(sorted_src_images, sorted_dst_images), desc='Adding EXIF info',
                                     total=len(sorted_src_images), colour='green'):
        add_exif_info(src_img_path=img_path1,
                      dst_img_path=img_path2)

    print("exif info added successfully!")


if __name__ == '__main__':
    # 设置图片文件路径，假设文件格式为 .jpg, .png, .jpeg等
    src_folder_path = r'C:\Users\YanJun\Desktop\Semantic-Segmentation-Data-Label\imgs'  # 替换为你实际的文件夹路径
    dst_folder_path = r'C:\Users\YanJun\Desktop\Semantic-Segmentation-Data-Label\voc1\SegmentationClassVisualization'  # 替换为你实际的文件夹路径
    main(src_folder_path=src_folder_path, dst_folder_path=dst_folder_path)
