# coding:utf-8
# 第15课 Python对象比较、拷贝

import copy

if __name__ == "__main__":
    a = 2
    b = 2
    # '==' 操作符⽐较对象之间的值是否相等
    print(a == b)
    # 'is' 操作符⽐较的是对象的身份标识是否相等，即它们是否是同⼀个对象，是否指向同⼀个内存地址
    print(a is b)
    # 对象的身份标识，都能通过函数id(object)获得
    print("id(a) = {}".format(id(a)))
    print("id(b) = {}".format(id(b)))
    # 对于整型数字来说，a is b为True的结论，因为Python会自动缓存范围在 [-5, 256] 之间的整数，因此这个范围内的同一个数字都使用同一个内存地址。
    # 超过这个范围就要看运行环境：如果在交互式或Jupyter中执行，每行代码是单独编译的，因此a和b是独立的对象，就不相等。
    # 而如果是脚本中，python会使用“常量折叠”优化的技术，此时a和b指向同一个对象。
    a = 10000000
    b = 10000000
    print(a == b)
    print(a is b)
    print("id(a) = {}".format(id(a)))
    print("id(b) = {}".format(id(b)))
    # 永远不要用 is 来比较数值或字符串的内容。
    # is 应该只用于检查一个变量是否为 None (例如 if x is None:)，或者检查两个变量是否确实是同一个实例（单例模式）。

    # 对于不可变变量
    t1 = (1, 2, [3, 4])
    t2 = (1, 2, [3, 4])
    print(t1 == t2)
    print(id(t1), id(t2))
    t1[-1].append(5)
    print(t1 == t2)
    print(id(t1), id(t2))

    # 浅拷贝：是指重新分配⼀块内存，创建⼀个新的对象，⾥⾯的元素是原对象中⼦对象的引⽤
    l1 = [1, 2, 3]
    l2 = list(l1)
    print(l1 == l2)
    print(l1 is l2)
    s1 = set([1, 2, 3])
    s2 = set(s1)
    print(s1, s2)
    print(s1 == s2)
    print(s1 is s2)
    # 通过切片操作
    l1 = [1, 2, 3]
    l2 = l1[:]
    print(l1 == l2)
    print(l1 is l2)
    # 使用copy函数
    l2 = copy.copy(l1)
    print(l1 == l2)
    print(l1 is l2)
    # 元组的不同，返回一个指向元组的引用
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print(t1 == t2)
    print(t1 is t2)

    # 浅拷贝的副作用
    l1 = [[1, 2], (30, 40)]
    l2 = list(l1)
    l1.append(100)
    l1[0].append(3)
    print(l1)
    print(l2)
    l1[1] += (50, 60)
    print(l1)
    print(l2)

    # 深拷贝
    l1 = [[1, 2], (30, 40)]
    l2 = copy.deepcopy(l1)
    l1.append(100)
    l1[0].append(3)
    print(l1, l2)
    # 陷入无限循环的深拷贝
    x = [1]
    # 把 x 这个对象本身的引用（内存地址）添加到了它自己的末尾
    x.append(x)
    print(x)
    y = copy.deepcopy(x)
    print(y)

    # 思考题
    # == 比较会比较所有元素是否相等，而x和y都是无限循环引用的对象，会报超出递归深度错误
    # print(x == y)  # 报错：RecursionError: maximum recursion depth exceeded in comparison
    print(x is y)
