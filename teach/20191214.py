#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20191214.py    
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/14 14:54   Taoweidong   1.0         None
"""


# import lib

def print_line(a):
    """
    打印一条横线
    @param a: 入参
    @return: 一条横线
    """
    print(a * 20)


def sum_sum(a, b, c):
    """
    三个数字求和
    @param a: 第一个数字
    @param b: 第二个数字
    @param c: 第三个数字
    @return: 求和结果
    """
    return a + b + c


def average_num(a, b, c):
    """
    计算三个数字的平均值
    @param a: 第一个数字
    @param b: 第二个数字
    @param c: 第三个数字
    @return: 平均值
    """
    return sum_sum(a, b, c) / 3


if __name__ == '__main__':
    print_line('-')
    print_line("X")
    print_line(10)
    arr = [10, 20, 30]
    print_line(arr)
    # 循环调用
    for i in range(10):
        print_line('*')
    print("-----------------")
    print(average_num(10, 20, 30))
