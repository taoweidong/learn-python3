#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20191214_输入.py    
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/14 15:41   Taoweidong   1.0         None
"""

# import lib

if __name__ == '__main__':
    # name = input("请输入你的名字：")
    # print(f"您输入的名字是:{name}")

    abc = "Hello World"
    # print(abc[0])
    # for item in abc:
    #     print(item)

    # 切片功能
    # 语法：序列名[开始位置的下标:结束位置的下标:步长]
    print(abc[::])
    print(abc[1:3:])
    print(abc[1:3:5])
    # 获取字符串中偶数位置的字符
    print(abc[::2])
    print(abc[2::1])
    # 字符串翻转
    print(abc[::-1])

    a = "AAA"
    b = a
    print(a)
    print(b)
    a = "A0000"
    print(a)
    print(b)

    # 函数的使用:查找函数
    myStr = "hello World , I am learning python!!"
    print(myStr.find("hello", 0, 5))
    print(myStr.find("A55"))
    print(myStr.find("A55"))
    # 函数的使用：index函数
    print(myStr.index("hello", 0, 5))
    # print(myStr.index("A55"))  # 查找不到会报错
    # print(myStr.index("A55"))

    # 统计函数
    print(myStr.count("h"))
    print(myStr.count("5"))
