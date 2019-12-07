# -*- coding: utf-8 -*-
# 2019年12月7日：学习笔记，基础语法学习
if __name__ == '__main__':
    # name = raw_input('输入你的名字:')
    # print 'Hello', name

    # python是一种动态语言，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
    # java是一种静态语言，变量定义的时候必须指定数据类型，如果赋值时的数据类型和定义的不匹配会报错
    # 字符串的定义
    print """Hello
    World
    Python"""
    # 数字的定义
    number = 100
    print(number)
    #     boolean类型的数据定义
    flag = True
    print(flag or number == 12)
    print(flag and number == 12)
    print(not number == 12)

    # 空值的定义:这是python中的一种特殊的只，不能理解为0
    abc = None
    print abc

    # 内存的理解

    # 循环语句
    if flag:
        print '这是真的'
    else:
        print '这是假的'
