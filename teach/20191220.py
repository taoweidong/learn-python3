#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""   
@Contact: taowd@outlook.com
@Author : Taoweidong
@Date   : 2019/12/20 22:12
"""

# import lib
if __name__ == '__main__':
    # 复制字符
    tmp = "H"
    arr = [10, 23]
    print(tmp * 5)
    print(arr * 5)

    # 合并两个列表
    arr1 = [10, 20]
    arr2 = [3, 5]
    print(arr1 + arr2)

    # 存在或者不存在
    tu = (10, 20, 30, 62)
    print(10 in tu)
    print(10 not in tu)

    # 公共方法
    print(max(tu))
    print(min(tu))
    print(len(tu))
    print("*" * 20)
    # range
    for item in range(5):
        print(item)

    print("*" * 20)
    # enumerate() 用于返回一个数据序列和下标
    for item in enumerate(tu):
        # print(item)
        print(item[0], item[1])

    print("*" * 20)
    # 数据类型转换
    list1 = [10, 20, 30, 20, 11]
    s1 = {200, 300, 500, 600}
    s2 = ('AA', 'BB')
    print(tuple(list1))
    print(list(s1))
    print(list(s2))
    print(set(list1))
    print(set(list1))

    print("*" * 100)
    # 推导式：用一个
    # 列表推导式
    list1 = []
    i = 0
    while i < 10:
        list1.append(i)
        i += 1
    print(list1)

    list1 = [i for i in range(20)]
    print(list1)
    list1 = [i for i in range(1, 20, 2)]
    print(list1)
    list1 = [i for i in range(1, 100) if i % 2 == 0]
    print(list1)
    print("*" * 100)
    # 字典推导式
    print("*" * 100)
    dict1 = {i: i ** 2 for i in range(1, 10)}
    print(dict1)

    # 将两个列表合并为一个字典
    list1 = ["name", "age"]
    list2 = ["Tom", 20]
    dict1 = {list1[i]: list2[i] for i in range(len(list1))}
    print(dict1)

    print("*" * 100)
    # 集合推导式
    list1 = {i for i in range(1, 20, 2)}
    print(list1)
