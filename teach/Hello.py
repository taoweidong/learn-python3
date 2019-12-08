# -*- coding: utf-8 -*-
# 2019年12月7日：学习笔记，基础语法学习
if __name__ == '__main__':
    # name = raw_input('输入你的名字:')
    # print 'Hello', name

    # 变量：就是一个存储数据的时候当前数据所在的内存地址的名称或者代号，用于快速访问到这个内存地址
    # 变量名 = 值

    # python是一种动态语言，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
    # java是一种静态语言，变量定义的时候必须指定数据类型，如果赋值时的数据类型和定义的不匹配会报错
    # 字符串的定义
    print
    """Hello
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
    print(abc)

    # 内存的理解

    a = 'ABC'
    # Python解释器干了两件事：
    # 1、在内存中创建了一个‘abc’的字符串
    # 2、在内存中创建了一个名字是'a'的变量，并把它指向'abc'
    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)

    # 数学计算演示
    print
    10 / 3
    print
    10.0 / 3
    print
    10 % 3

    # list列表演示:有序的集合，可以随时添加和删除其中的元素
    listData = ['Hello', 'World']
    print(listData)
    # 列表的长度
    print(len(listData))
    print(listData[0])
    print(listData[-1])
    # 注意月越界风险
    # print(listData[3])

    # 列表数据的添加
    listData.append('张三')
    print(listData)

    # 变量类型查询
    print(type(listData))
    print(type(a))
    print(type(b))
    print(type(abc))

    # 循环语句
    if flag:
        print
        '这是真的'
    else:
        print
        '这是假的'
