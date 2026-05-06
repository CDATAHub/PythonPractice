# coding:utf-8

# 如果你在异常处理的except block中，把异常赋予了⼀个变量，那么这个变量会在except block执⾏结束时被删除
# 也就是说在异常所指向的那个变量会在finally中删除，因此⼀定要保证except中异常赋予的变量，在之后的语句中不再被⽤到
# 异常变量作用域清理：异常变量的作用域仅限于except块内部
e = 1
try:
    1 / 0
except ZeroDivisionError as e:
    pass

print(e)  # 这一行会报错：NameError: name 'e' is not defined
