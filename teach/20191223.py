#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""   
@Contact: taowd@outlook.com
@Author : Taoweidong
@Date   : 2019/12/23 22:15
函数的进一步学习：局部变量
"""

# 全局变量：指的是在函数体内，外都能生效的变量
gg = "Hello"


def testA():
    # 变量a是函数内部的变量，函数外部访问则立即报错
    # a = 100
    # print(a)

    # 注意：在函数体修改全局变量，必须增加特殊的处理
    global gg  # 声明gg为全局变量
    gg = "World"
    print(gg)


# import lib
if __name__ == '__main__':
    print(gg)

    # 局部变量：定义在函数体内部的变量，即只有在函数体内部生效
    testA()

    print(gg)
