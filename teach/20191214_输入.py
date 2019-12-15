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
    myStr = "hello World, I am learning python!!"
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

    # replace函数：替换函数
    print(myStr.replace("h", "X"))
    print(myStr.replace("h", "X", 1))
    # split函数:分割函数:默认使用空格
    print(myStr.split())
    print(myStr.split(" ", 2))
    print(myStr.split(" ", 10))

    # 合并列表的数据为一个字符串 join
    arr = ["Hello", "World", "Python"]
    result = " ".join(arr)
    print(result)

    # 首字符转大写
    print(result.capitalize())
    # 每个单词首字符转大写
    print(result.title())
    # 所有字符转大写
    print(result.upper())
    # 所有字符转小写
    print(result.lower())

    result = "   Hello World     "
    # 去除两边空格
    print(result.strip())
    print(result.lstrip())
    print(result.rstrip())

    # 补全字符串
    result = result.strip()
    print(result.ljust(20, "X"))
    print(result.rjust(20, "X"))

    # 是否为指定字符串开头
    print(result.startswith("Hel", 0, 10))
    print(result.endswith("d"))
    arr = ["x", "y"]
    # print(result.center(3, **arr))

    print("----------------------------")
    # 是否都是字母
    result = "Hello"
    print(result.isdigit())
    print(result.isalpha())
    result = "555"
    print(result.isdigit())
    result = "Hello555"
    print(result.isalnum())
    print(result.isspace())
