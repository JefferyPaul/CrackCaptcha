# "可切割图片"类，可实现如下方法：
# 1 颜色识别
# 2 转为黑白
# 3 切割
from PIL import Image


# 0 打开图片
def im_open(path):
    return Image.open(path)


# 1 颜色识别
def color_identity(im):
    width, height = im.size
    print(width, height, im.format, im.format_description)

    # 将图片转换为8位像素模式"P"
    im.convert("P")
    # histogram柱状图，记录256色每个色号出现的次数
    his = im.histogram()
    # 用value字典记录每个色号及其出现次数，用于对色号排序
    values = {}
    for i in range(256):
        values[i] = his[i]
    for j, k in sorted(values.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(j, k)


# 2 将im转换为黑白的im2
def change_black(im):
    im_black = Image.new("P", im.size, 255)
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y, x))
            if pix == 181:
                im_black.putpixel((y, x), 0)
    return im_black


# 3 切割
def crop_image(im):
    in_letter = False
    found_letter = False
    start = 0
    end = 0
    letters = []

    # 接下来要得到单个字符的像素集合，由于例子比较简单，我们对其进行纵向切割，先确定切割点位：
    for y in range(im.size[0]):
        for x in range(im.size[1]):
            pix = im.getpixel((y, x))
            if pix != 255:
                in_letter = True
        if found_letter is False and in_letter is True:
            found_letter = True
            start = y
        if found_letter is True and in_letter is False:
            found_letter = False
            end = y
            # 得出各个图片的[(start位置，end位置),]
            letters.append((start, end))
            start = 0
            end = 0
        in_letter = False
    print(letters)

    # 切割
    single_ims = []
    for letter in letters:
        if letter[1] - letter[0] > 10:
            single_im = im.crop((letter[0], 0, letter[1], im.size[1]))
            single_ims.append(single_im)

    return single_ims
