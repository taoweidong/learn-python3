#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20191215.py    
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/15 15:00   Taoweidong   1.0         None
"""

# import lib
if __name__ == '__main__':
    arr = ["张三", "李四", "王五"]
    print(arr)
    # 迭代
    for item in arr:
        print(item)
    # index
    print(arr.index("张三"))
    # print(arr.index("张三0"))
    print(arr.count("张三"))
    print(len(arr))
    # 判断是否存在
    print("张三" in arr)
    print("张三" not in arr)
    print("张三0" not in arr)
    # 增加数据:在末尾添加数据
    print(arr.append("Hello"))
    print(arr)
    # 指定位置添加数据
    print(arr.insert(1, "Tom"))
    print(arr)

    arr.extend(["Hello", "World"])
    print(arr)

    # 删除
    # del arr
    # print(arr)

    # 删除指定下标的数据
    del arr[0]
    print(arr)

    # 删除指定下标的数据，如果不指定下标，表示删除最后一个数据
    print(arr.pop())
    print(arr)

    print(arr.pop(1))
    print(arr)

    # 删除指定数据
    arr.remove("Hello")
    print(arr)

    # 清空列表
    arr.clear()
    print(arr)

    list1 = [10, 2, 36, 4, 85, 966, 5, 36, 100]
    # 逆置排序
    list1.reverse()
    print(list1)

    # 排序
    list1.sort()
    print(list1)

    list1.sort(reverse=True)
    print(list1)

    # 复制数据
    list2 = list1.copy()
    print(list2)
    list2[0] = 5555
    print(id(list2))
    print(id(list1))

    print(list2)
    print(list1)
    print("*******************************************")
    # 迭代
    i = 0
    while i < len(list2):
        print(list2[i])
        i += 1
    print("*******************************************")
    # for迭代
    for item in list2:
        print(item)

    # 列表嵌套
    name_list = [["小敏", "小明", "小红"], ["Tom", "Honey", "Joy"], [10]]
    for item in name_list:
        for it in item:
            print(it)
