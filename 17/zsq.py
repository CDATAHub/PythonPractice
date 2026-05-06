# coding:utf-8
# 第17课 强大的装饰器


import functools
import time

if __name__ == "__main__":
    # 函数作为变量
    def func(message):
        print("收到一个消息:{}".format(message))


    send_message = func
    send_message("hello world")

    # 函数作为参数
    def root_call(fun, message):
        print(fun(message))


    root_call(func, "函数参数")

    # 函数嵌套
    def fund(message):
        def get_message(message):
            print("收到一个消息:{}".format(message))

        return get_message(message)


    fund("函数嵌套")

    # 闭包
    # 闭包的三个条件：
    # 1、必须有嵌套函数。
    # 2、内层函数必须引用外层函数的变量。
    # 3、外层函数必须返回内层函数本身，而不是返回内层函数的运行结果。
    def func_closure():
        def get_message(message):
            print("收到一个消息:{}".format(message))

        return get_message


    send_message = func_closure()
    print(send_message.__closure__)
    send_message("返回函数对象(闭包)")


    def func_closure(external_info):  # 变量在外面
        def get_message():
            # 这里引用了外层的 external_info
            print("收到外部环境的信息: {}".format(external_info))

        return get_message


    # 闭包在这一步已经“捕获”了 "我是被私藏的信息"
    send = func_closure("我是被私藏的信息")
    print(send.__closure__)
    # 调用时不需要传参，它依然记得 "我是被私藏的信息"
    send()

    # 简单装饰器例子
    def my_decorator(func):
        def wrapper():
            print("装饰器")
            func()

        return wrapper


    def greet():
        print("你好")


    greet = my_decorator(greet)
    greet()

    # 原函数还是原函数吗？
    print(greet.__name__)
    print(help(greet))

    # 使用functools.wrap
    def my_decorator2(func):
        # 如果没有 wraps：greet2.__name__ 会输出 "wrapper"。因为 greet2 已经被替换成了 wrapper 函数。这会破坏函数的元数据（如文档字符串、函数名等），导致调试困难。
        # 有了 wraps：它会自动把原函数 func（即 greet2）的属性复制到 wrapper 上。
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("functools的装饰器")
            func(*args, **kwargs)

        return wrapper


    @my_decorator2
    def greet2(message):
        print(message)


    greet2("functools")
    print(greet2.__name__)

    # 类装饰器
    class Count():
        def __init__(self, func):
            self.func = func
            self.num_calls = 0

        def __call__(self, *args, **kwargs):
            self.num_calls += 1
            print("num of call is: {}".format(self.num_calls))
            return self.func(*args, **kwargs)


    @Count
    def example():
        print("类装饰器")


    example()
    example()

    # 装饰器嵌套
    def my_decorator_a(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("functools的装饰器a")
            func(*args, **kwargs)

        return wrapper


    def my_decorator_b(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("functools的装饰器b")
            func(*args, **kwargs)

        return wrapper


    @my_decorator_a
    @my_decorator_b
    def greet3(message):
        print(message)


    greet3("functools")
    print(greet3.__name__)

    # 应用举例 给函数加上计时功能
    def log_execution_time(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            res = func(*args, **kwargs)
            end = time.perf_counter()
            print("函数{}运行耗时{}秒".format(func.__name__, end - start))
            return res

        return wrapper


    @log_execution_time
    def add(n):
        s = 0
        for i in range(n):
            s += i
        return s


    res = add(10000)
    print(res)


    @log_execution_time
    def multiply(n):
        s = 1
        for i in range(n):
            s = s * (i + 1)
        return s


    res = multiply(10000)
    print(res)
