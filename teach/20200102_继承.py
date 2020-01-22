#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""   
@Contact: taowd@outlook.com
@Author : Taoweidong
@Date   : 2020/1/2 22:52
继承的学习
"""


# import lib

class A(object):
    name = ""
    age = 0

    def __init__(self):
        self.level = "好人"

    def info_print(self):
        print("我的名字是%s,年龄是%d" % (self.name, self.age))

    def test(self):
        print("我是A类的方法")


class B(A):
    def __init__(self):
        B.__init__(self)

    def info_print(self):
        print("我的名字是%s,年龄是%d" % (self.name, self.age))

    def test(self):
        print("我是B类的方法")


class C(B):
    pass
    # def test(self):
    #     print("我是c类的方法")


if __name__ == '__main__':
    # a = A()
    # a.name = "张三"
    # a.age = 12
    # print(a.name, a.age)
    #
    b = B()
    b.name = "李四"
    b.age = 25
    print(b.info_print())

    c = C()
    c.test()
    print(c)
    # 打印继承关系
    print(C.__mro__)
    print(B.__mro__)
