# -*- coding:utf-8 -*-
# 基础篇 03 列表list和元组tuple

# import numpy as np
import dis

if __name__ == "__main__":
    l = [1, 2, "hello", "world"]
    tup = ("jason", 22)
    print(l)
    print(tup)

    # 列表元素可变，元组元素不可变
    l = [1, 2, 3, 4]
    l[3] = 40
    print(l)
    tup = (1, 2, 3, 4)
    # tup[3] = 40
    print(tup)

    # 列表和元组都支持负数索引，-1 表示最后一个元素，-2 表示倒数第二个元素
    print(l[-1])
    print(tup[-2])

    # 增加元素
    # 创建新的元组 new_tup，并依次填充原元组的值，逗号表示这是单元素元组
    new_tup = tup + (5,)
    print(new_tup)
    # 添加元素 5 到原列表的末尾
    l.append(5)
    print(l)

    # 片切操作，包含元素规则是左闭右开
    l = [1, 2, 3, 4]
    # 返回列表中索引从 1 到 2 的子列表
    print(l[1:3])
    tup = (1, 2, 3, 4)
    print(tup[1:3])

    # 嵌套，列表和元组可以互相嵌套
    l = [[1, 2, 3], [4, 5], (6, 7)]
    tup = ((1, 2, 3), (4, 5, 6), [7, 8])
    print(l)
    print(tup)

    # 相互转换
    print(list((1, 2, 3)))
    print(tuple([1, 2, 3]))

    # 内置函数
    l = [3, 2, 3, 7, 8, 1]
    print(l.count(3))
    print(l.index(7))
    # 元组没有reverse和sort内置函数，因为元组元素不可变
    l.reverse()
    print(l)
    l.sort()
    print(l)

    tup = (3, 2, 3, 7, 8, 1)
    print(tup.count(3))
    print(tup.index(7))
    print(list(reversed(tup)))
    print(sorted(tup))

    # 列表和元组的存储差异
    l = [1, 2, 3]
    tup = (1, 2, 3)
    print(l.__sizeof__())  # 104
    print(tup.__sizeof__())  # 48

    l = []
    print(l.__sizeof__())  # 40
    l.append(1)
    print(l.__sizeof__())  # 72
    l.append(2)
    print(l.__sizeof__())  # 72
    l.append(3)
    print(l.__sizeof__())  # 72
    l.append(4)
    print(l.__sizeof__())  # 72
    l.append(5)
    print(l.__sizeof__())  # 104

    # 查看字节码
    dis.dis("empty_list = list()")
    dis.dis("empty_list = []")