# -*- coding: utf-8 -*-
if __name__ == '__main__':
    # 运算符
    print(100 + 588)
    print(100 - 588)
    print(100 * 588)
    print(100 / 588)
    print(9 // 4)
    print(9 % 4)
    print(2 ** 6)

    #     复合赋值运算符
    a = 10
    a += 2
    print(a)
    a **= 5
    print(a)

    # 注意下面计算时的顺序
    # 先算复合赋值运算符右面的表达式：然后再算复合赋值运算符
    d = 10
    d *= 1 + 2
    print(d)

    #  逻辑运算符
    print(12 and 23)
    print(12 and 0)

    print(12 or 0)
    print(12 or 25)

    print(not 25)
