# -*- coding: utf-8 -*-


def showMessage(ab, mm):
    print("Hello python function", mm)


# 默认参数: 函数定义:函数定义的上方必须有两行空行
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 可以省略的参数
def test01(a=1, b=20):
    print("Hello python:" + str(a + b))


# 多个参数的函数定义
def test02(a, b):
    print("Hello python:" + str(a + b))


# 可变参数:传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def test002(*args):
    print(args)


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c=0, *args, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kwargs)


# 函数的返回值
def func01():
    """函数的说明文档:这个函数是返回两个数字"""
    return 10, 26


# 默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
if __name__ == '__main__':
    help(len)
    help(func01)

    mm = func01()
    print(mm)

    a, b = func01()
    print(a, b)

    func(1, 2)
    func(b=12, a=23)
    func(12, 23, 56)
    # func() 调用错误，缺少参数
    args = (1, 2, 3, 4)
    kw = {'x': 99}
    func(*args, **kw)

    print(abs(100))
    print(abs(-200))
    showMessage()
    test01(3, 20)
    test002()
    test01(b=30)
    test01(a=52)
    # 可变参数
    test002(12, 25, 36)

    print("---------------")
    nums = [10, 25, 36, 100]
    test002(*nums)
    # 关键字参数
    print("---------------")
    person('张三', 25)
    person('张三', 25, city='西安')
    kw = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=kw['city'], job=kw['job'])
    person('Jack', 24, **kw)
