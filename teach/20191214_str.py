#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   20191214_str.py    
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/12/14 15:23   Taoweidong   1.0         None
"""

# import lib


if __name__ == '__main__':
    # 字符串定义
    a = "Hello"
    b = 'World'
    c = '''Hello
    world'''
    d = """ 靜夜思
  李白
窗前明月光
疑似地上霜
举头望明月
低头思故乡
"""
    print(type(a))
    print(a)
    print(type(b))
    print(b)
    print(type(c))
    print(c)
    print(type(d))
    print(d)

    tmp = "Tom"
    print("我的名字是%s" % tmp)
