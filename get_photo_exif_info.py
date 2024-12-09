# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/5 9:23
# @Author  : Yanjun Hao
# @Site    : 
# @File    : get_photo_exif_info.py.py
# @Software: PyCharm 
# @Comment :

import piexif
from rich import print
from PIL import Image

b = b"\x3c\x2f\x72\x64\x66\x3a\x44\x65\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x3e"
a = b"\x3c\x72\x64\x66\x3a\x44\x65\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x20"

aa = ["\x3c\x72\x64\x66\x3a\x44\x65\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x20"]
bb = ["\x3c\x2f\x72\x64\x66\x3a\x44\x65\x73\x63\x72\x69\x70\x74\x69\x6f\x6e\x3e"]

# rb是读取二进制文件
imd_path = r"C:\Users\YanJun\Desktop\Semantic-Segmentation-Data-Label\imgs\H_005_00484.JPG"
img_path = r"C:\Users\YanJun\Desktop\Semantic-Segmentation-Data-Label\voc1\SegmentationClassVisualization\H_005_00484.JPG"

img = open(imd_path, 'rb')
# bytearray() 方法返回一个新字节数组
data = bytearray()
# 标识符,
flag = False

for i in img.readlines():
    # 按行读取二进制信息，标签成对出现
    if a in i:
        flag = True
    if flag:
        # 把第i行数据复制到新数组中
        data += i
    if b in i:
        break
# print("data", data)

if len(data) > 0:
    data = str(data.decode('ascii'))
    # print(data)
    # filter()函数用于过滤序列，过滤掉不符合条件的元素，返回符合条件的元素组成新列表。
    # filter(function,iterable) ,function -- 判断函数。iterable -- 可迭代对象
    # python允许用lambda关键字创造匿名函数。
    # 在 lambda 关键字之后、冒号左边为参数列表，可不带参数，也可有多个参数。若有多个参数，则参数间用逗号隔开，冒号右边为 lambda 表达式的返回值。
    # left--->right
    # judge condition 'drone-dji:' in x
    lines = list(filter(lambda x: 'drone-dji:' in x, data.split("\n")))
    # print("lines", lines)
    dj_data_dict = {}
    for d in lines:
        # remove 'drone-dji:'
        d = d.strip()[10:]
        # k is name
        # v is value
        k, v = d.split("=")
        # print(f"{k} : {v}")
        dj_data_dict[k] = v

    print(dj_data_dict)
