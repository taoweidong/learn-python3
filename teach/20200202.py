#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
文件读写练习
文件操作包含：打开，关闭，读写复制
@Contact: taowd@outlook.com
@Author : Taoweidong
@Date   : 2020/2/2 20:16
"""

# import lib
import os

if __name__ == '__main__':
    # # 打开文件
    # file = open("hello.txt", 'w')
    # # 写入文件
    # file.writelines("Hello World python!!!")
    # file.writelines(os.name)
    #
    # # 关闭文件操作
    # file.close()

    # file = open("hello.txt", 'a')
    # data = file.read()
    # print(data)

    # print(os.name)
    # print(os.environ)

    # 文件的读取
    file = open("hello.txt", 'r')
    # 读取所有数据
    # print(file.read())
    # 读取一行数据
    # print(file.readline())
    # 读取多行数据:返回一个数组
    items = file.readlines()
    print(items)
    for item in items:
        print(item)
    # 关闭文件流
    file.close()
