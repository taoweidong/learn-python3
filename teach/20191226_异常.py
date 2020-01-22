#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""   
@Contact: taowd@outlook.com
@Author : Taoweidong
@Date   : 2019/12/26 22:42
1、了解异常
2、捕获异常
3、异常的else
4、异常的finally
5、异常的传递
6、自定义异常
"""

# import lib
if __name__ == '__main__':
    try:
        open('test.txt', 'r')
    except IOError:
        print("出现了IO异常")
    except NameError:
        print("ccc")

    print("*" * 100)
    try:
        print(1 / 0)
    except (NameError, ZeroDivisionError) as result:
        print("算法有异常:", result)
