#实现颜色少的，可纵向切割的图片识别
#将其定义为 "可切割图片"类，可实现如下方法：
# 1 颜色识别
# 2 转为黑白
# 3 切割

#切割后的图片 可实例化为 "可识别图片"，可实现如下方法：
# 1 设定训练集
# 2 计算矢量
# 3 对比


from crop_image import *
from get_imageset import get_imageset
from VectorCompare import VectorCompare
from build_vector import build_vector


def crack(crack_im):
    guess = []
    # image 字典，包含某个icon.str的训练集信息，为所有可能检测出来的字符。用于逐一与crack对比，找出relation最大的icon.str
    for image in imageset:
        # x为image.key 即icon.str， y为其image.value 列表 即某一个icon用于训练的所有图形的vector值字典
        for x, y in image.items():
            if len(y) != 0:
                # v.relation(字典1，字典2), { word:count }
                guess.append((v.relation(y[0], build_vector(crack_im)), x))
                # guess = [ [相关系数，某个训练图形所代表的icon.str], ]
    print(sorted(guess, key=lambda re: re[0]))
    print(sorted(guess,key=lambda re : re[0])[-1][1])

# 传入待识别图片，识别颜色，转为黑白图片
im_initial = im_open('captcha.GIF')
color_identity(im_initial)
im_black = change_black(im_initial)

# 加载训练集。
# imagest列表用于记录 [{ 某个icon.str:[ 用于训练的图形的vector值字典{count:Image.getdata[i]}, ] }, ]
imageset = get_imageset()
v = VectorCompare()
# 切割-识别
for im_single in crop_image(im_black):
    crack(im_single)
