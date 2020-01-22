#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""   
@Contact   : taowd@outlook.com
@Author    : Taoweidong
@Date      : 2019/12/19 21:53
1、类是创建实例的模板，而实例是一个个具体的对象，各个实例拥有的数据都相互独立，互不影响
2、方法就是与实例绑定的函数，和普通的函数不同，方法可以直接访问实例的数据
3、魔法方法：init del str等
"""


class Parent(object):
    # 定义类变量
    future = "梦想"

    def __init__(self):
        """
        魔法方法：初始化类对象
        """
        # 定义对象变量
        self.name = ""
        self.age = 0
        self.sex = "man"

    def wash(self):
        """
        这是一个实例方法.
        @return: 打印一句话
        """
        print(self)
        print(type(self))
        print("这是一个实例方法----", self.future)

    def get_level(self):
        if self.age < 13:
            return "未成年"
        elif self.age < 20:
            return "还未进入社会"
        else:
            return "进入社会了"


class Woman(Parent):
    def __init__(self):
        # 此处调用父类的构造方法
        super(Woman, self).__init__()
        self.boyFriend = ""

    def sayHello(self):
        print("我的名字是%s,今年%d岁,%s,我的男朋友是%s" % (self.name, self.age, self.get_level(), self.boyFriend))


class Man(Parent):
    def __init__(self):
        # 此处调用父类的构造方法
        super(Man, self).__init__()
        self.girlFriend = ""

    def sayHello(self):
        print("我的名字是%s,今年%d岁,%s,我的女朋友是%s" % (self.name, self.age, self.get_level(), self.girlFriend))

    # 类似java中的toString方法
    def __str__(self):
        return str(self.__dict__)

    # 类似java中的Object的销毁方法
    def __del__(self):
        print("当前对象已被删除：", id(self))


if __name__ == '__main__':
    parent = Parent()
    parent.age = 25
    Parent.future = "做一名合格的程序猿"
    # print(parent)
    # print(type(parent))
    # print(parent.name)
    # print(parent.age)
    # print(parent.sex)
    # print(Parent.future)
    #
    # parent.wash()
    # parent.get_level()
    # person1 = Parent()
    # person1.wash()
    print("*******************")
    woman = Woman()
    woman.name = "小红"
    woman.age = 20
    woman.boyFriend = "还没有"

    man = Man()
    man.name = "张三"
    man.age = 25
    man.girlFriend = "刘亦菲"
    woman.sayHello()
    man.sayHello()

    # 打印继承关系
    print(Woman.mro())
    # 判断一个变量是否是某个类型
    print(isinstance(man, Woman))
    print(isinstance(man, Man))

    print(man)
