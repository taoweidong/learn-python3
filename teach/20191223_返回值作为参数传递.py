#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""   
@Contact: taowd@outlook.com
@Author : Taoweidong
@Date   : 2019/12/23 22:57
"""


def test1():
    return 50


def test2(num):
    """
    这是一个方法的注释
    @param num: 方法的入参数
    @return:  返回值
    """
    print(num)


def getNum():
    return 10


# import lib
if __name__ == '__main__':
    # result = test1()
    # test2(result)
    print(getNum())
