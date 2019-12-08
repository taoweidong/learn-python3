# -*- coding: utf-8 -*-
"""
1. 定义变量
2. 使用变量
3. 看变量特点
"""

if __name__ == '__main__':
    # 格式化输出
    age = 22
    name = 'Tom'
    weight = 62.2
    print('我的姓名是%s' % name)
    print('今年我的年龄是%d岁' % age)
    print('今年我的体重是%.2f公斤' % weight)
    # 格式化多个数据
    print('我的名字是%s,今年%d岁' % (name, age))

    # f-字符串为python3.6版本之后才能使用
    # print(f'我的名字是{name},今年{age}岁')
    print('Hello', end="\n")
    print('World')

    # inputStr = raw_input("请输入姓名:")
    # print('您输入的内容是：%s' % inputStr)

    number003 = input("输入年龄：")
    print(type(number003))
    print(type(int(number003)))
    print(float(number003))
    print(type(float(number003)))
    print(number003)
