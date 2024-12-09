# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/9 9:06
# @Author  : Yanjun Hao
# @Site    : 
# @File    : add_exif_info_use.py.py
# @Software: PyCharm 
# @Comment :

import piexif
from rich import print
from PIL import Image

b = b"\x3c\x2f\x72\x64\x66\x3a\x44\x65\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x3e"
a = b"\x3c\x72\x64\x66\x3a\x44\x65\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x20"

img_path = r"C:\\Users\\YanJun\\Desktop\\Semantic-Segmentation-Data-Label\\imgs\\H_005_00484.JPG"
new_image_path = r"C:\Users\YanJun\Desktop\Semantic-Segmentation-Data-Label\voc1\SegmentationClassVisualization\H_005_00484.JPG"

img = open(img_path, 'rb')
data = bytearray()
flag = False

for i in img.readlines():
    if a in i:
        flag = True
    if flag:
        data += i
    if b in i:
        break

if len(data) > 0:
    data = str(data.decode('ascii'))
    lines = list(filter(lambda x: 'drone-dji:' in x, data.split("\n")))
    dj_data_dict = {}
    for d in lines:
        d = d.strip()[10:]
        k, v = d.split("=")
        dj_data_dict[k] = v

    print("Extracted EXIF data:", dj_data_dict)

    # Create EXIF data structure
    exif_dict = piexif.load(img_path)  # Load original EXIF data if exists
    user_comment = "; ".join([f"{k}={v}" for k, v in dj_data_dict.items()])

    # Add custom data to EXIF under the UserComment tag (0x9286)
    exif_dict['Exif'][piexif.ExifIFD.UserComment] = user_comment.encode('utf-8')

    # Save the updated EXIF data to a new image
    original_image = Image.open(img_path)
    exif_bytes = piexif.dump(exif_dict)
    original_image.save(new_image_path, "jpeg", exif=exif_bytes)

    print(f"Updated EXIF data saved to {new_image_path}")
else:
    print("No EXIF data found in the source image.")
