
#用python类实现向量空间
#它会比较两个python字典类型并输出他们的相似度（用0~1的数字表示）
import math

class VectorCompare:
    #计算矢量大小
    def magnitude(self, concordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    #计算矢量之间的cos值
    def relation(self,concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


"""
#-*- coding:utf-8 -*-
from PIL import Image

im = Image.open("captcha.gif")
#（将图片转换为8位像素模式）
im.convert("P")

#打印颜色直方图
#颜色直方图的每一位数字都代表了图片中含有对应位的颜色的像素的数量
print(im.histogram())

his = im.histogram()
values = {}

for i in range(256):
    values[i] = his[i]

for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
    print(j,k)
"""

#前面得到了图片中最多的10种颜色
#220，227是我们需要的红色和灰色，可以通过这一讯息构造一种黑白二值图片
#-*- coding:utf-8 -*-
from PIL import Image

im = Image.open("captcha.gif")
im.convert("P")
im2 = Image.new("P",im.size,255)

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227: #these are the numbers to get
            im2.putpixel((y,x),0)
im2.save('new.gif')


#得到单个字符的像素集合，进行纵向切割
inletter = False
foundletter = False
start = 0
end = 0

letters = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y,x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y
    
    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))

    inletter = False
print(letters)
#得到每个字符开始和结束的列序号


#对图片进行切割，得到每个字符所在的那部分图片
import hashlib
import time

count = 0
for letter in letters:
    #前两个值为左上角坐标
    #后两个值为右下角坐标
    im3 = im2.crop((letter[0], 0, letter[1],im2.size[1]))
    im3.save("./%s.gif"%(count))
    count += 1























