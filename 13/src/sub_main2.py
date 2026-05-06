# coding:utf-8
# 第13课 Python模块化

import sys
sys.path.append("..")

import utils.class_utils
import utils.utils
# from module_name import * 和 import module_name的区别就是：前者访问必须带前缀：module_name.func()，后者可直接调用：func()，
# 后者会导致命令冲突，以及不知道该方法出自哪里，推荐第一种方式。还有一种from module_name import class_name也可以

if __name__ == "__main__":
    print(utils.utils.get_sum(1, 2))

    encoder = utils.class_utils.Encoder()
    decoder = utils.class_utils.Decoder()

    print(encoder.encode("abcde"))
    print(decoder.decode("edcba"))
