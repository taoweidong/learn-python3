#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20191217.py    
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/17 22:40   Taoweidong   1.0         None
"""

# import lib
if __name__ == '__main__':
    # 元组：一个元组可以存储多个数据，元组内的数据是不能修改的
    num_list = (12, 25, 36, 200)
    print(num_list)
    print(len(num_list))
    print(num_list.count(12))
    print(num_list)

    num_list = ("Hello")
    # 数据类型
    print(type(num_list))

    print("************")
    # 查找
    print(num_list.index("Hello"))

    # 迭代
    for item in num_list:
        print(item)
