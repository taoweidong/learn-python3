#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""   
@Contact: taowd@outlook.com
@Author : Taoweidong
@Date   : 2020/1/2 23:24
子类调用父类同名方法和属性
"""


class Master(object):
    def __init__(self):
        self.kongfu = "[Master的功夫]"

    def make_cake(self):
        print(f'运用{self.kongfu}练习功夫')


class School(object):
    def __init__(self):
        self.kongfu = "[School的功夫]"

    def make_cake(self):
        print(f'运用{self.kongfu}练习功夫')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "[Prentice的功夫]"

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}练习功夫')

    def make_master_cake(self):
        # 初始化父类的属性和方法
        Master.__init__(self)
        Master.make_cake(self)
        # print(f'运用{self.kongfu}练习功夫')


# import lib
if __name__ == '__main__':
    pre = Prentice()
    pre.make_master_cake()
    pre.make_master_cake()
