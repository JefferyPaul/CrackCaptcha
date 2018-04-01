# 加载训练集
from build_vector import build_vector
from PIL import Image
import os


def get_imageset():
    iconset= ["0","1","2","3","4","5","6","7","8","9"]
    # imagest列表用于记录 [{ 某个icon.str:[ 用于训练的图形的vector值字典{count:Image.getdata[i]}, ] }, ]
    imagest = []
    for letter in iconset:
        temp = []
        # 同一个 icon.str 可能有多个用于训练的 图形
        for img in os.listdir('./iconset/%s' % letter):
            temp.append(build_vector(Image.open("./iconset/%s/%s" % (letter, img))))
        imagest.append({letter: temp})

    return imagest
