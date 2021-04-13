# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

image = Image.open('out/t2.png')
# image = image.convert('L') # 将图片转化为灰度图像
# threshold = 100
# table=[]
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image = image.point(table,'1')
# image.show()
text = pytesseract.image_to_string(image)
print(text)