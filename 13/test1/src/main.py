# coding:utf-8
# 第13课 Python模块化
# src/main.py
import sys
print(sys.path)
# sys.path.append("..")表示将当前程序所在位置向上提了⼀级，之后就能调⽤ utils 的模块了
# 利用sys.path.append("..")可以改变当前Python解释器的位置。不过，不推荐这种方式，固定⼀个确定路径对⼤型⼯程来说是⾮常必要的
from proto.mat import Matrix
from utils.mat_mul import mat_mul

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])

print(mat_mul(a, b).data)
