# -*- coding: utf-8 -*-
if __name__ == '__main__':
    name = ['张三', '李四', '王五', '马六']
    print(name)
    # 迭代方式
    for item in name:
        print("我的名字是：" + item)
    # 特殊迭代
    for item in range(0, len(name)):
        print("我的名字是：" + name[item] + ",序号是：" + str(item))
    # 迭代+条件
    for item in name:
        if item == '张三':
            print("我是张三，我是校长")
            continue
        else:
            print("我是：" + item + "，我是学生")
    else:
        # 注意：只有上面的for循环中的所有迭代执行完毕后才执行，
        # 循环中break跳出后不执行此处代码
        # 循环中continue跳过一次循环，执行此处代码
        print("所有学生点名结束，开始上课")

    # 三目运算符
    age = 10
    print("成年了" if age > 20 else "未成年")

    # 多重判断
    if age < 13:
        print("小学生")
    elif 13 <= age <= 20:
        print("初中生")
    elif 20 < age <= 25:
        print("高中生")
    elif age > 25:
        print("大学生")
    else:
        print("未知")

    # while循环
    index = 1
    while index <= 100:
        print("你好，python " + str(index))
        index += 1

    print(type(index))
    print(id(index))

    # 计算1-100累计和
    i = 0
    result = 0
    while i <= 100:
        result += i
        i += 1
    print(result)

    print(4 % 2)
    # 偶数累计求和
    i = 0
    result = 0
    while i <= 100:
        if i % 2 == 0:
            result += i
            i += 2
    print(result)

    # 嵌套循环
    index = 0
    while index < 3:
        index2 = 0
        while index2 < 3:
            print("I love You")
            index2 += 1
        print("No you not love")
        index += 1

    # 循环嵌套的使用
    # 打印星号
    # 方案1
    for i in range(5):
        for j in range(5):
            print("*", end="")
        print()

    print("---------------------")
    # 方案2
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            print("*", end="")
            j += 1
        print()
        i += 1
    print("---------------------")
    # 打印三角形
    i = 1
    while i <= 5:
        j = 0
        while j < i:
            print("*", end="")
            j += 1
        print()
        i += 1

    print("---------------------")
    # 打印九九乘法表
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(str(j) + "*" + str(i) + "=" + str(i * j), end="\t")
            j += 1
        print()
        i += 1
