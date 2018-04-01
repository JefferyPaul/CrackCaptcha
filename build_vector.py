# 向量空间图形识别
# 将图片转换为矢量
# Image.getdata()
# build_vector返回字典 { count : Image.getdata[i] }


def build_vector(im):
    d1 = {}
    count = 0

    for i in im.getdata():
        if type(i) == int:
            d1[count] = i
        elif type(i) == list:
            d1[count] = i[0]
        elif type(i) == tuple:
            d1[count] = i[0]
        count += 1

    return d1
