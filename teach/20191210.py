# -*- coding: utf-8 -*-
if __name__ == '__main__':
    print("Hello")
    # 条件判断
    age = 10
    if age > 19:
        print("成年人")
    elif age == 19:
        print("刚好成年")
    else:
        print("未成年人")

    # 循环
    name = ['张三', '李四', '王五']
    for item in name:
        print("我的名字是：" + item)

    print("---------------------------")
    # 循环
    name = ['张三', '李四', '王五']
    for item in name:
        print("我的名字是：" + item)
    else:
        print("这是一个特殊的分支，当for循环中的所有正确执行完毕之后执行的内容")

    print("---------------------------")
    # 计算1到100的和
    sumCount = 0
    for x in range(101):
        sumCount += x
    else:
        print("1-100的和是：" + str(sumCount))

    # while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
    print("---------------------------")

    sumCount = 0
    n = 100
    while n > 0:
        sumCount += n
        n -= 1
    else:
        print("1-100的和是：" + str(sumCount))

    print("---------------------------")

    d = dict()
    d.update({'tom': 20, 'jon': 25, '张三': 25})

    # 编辑
    d['王五'] = 10
    d['tom'] = 55
    # 通过in判断key是否存在：
    print('dd' in d)
    print('tom' in d)
    # 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
    print(d.get('dd', 99))
    # 删除一个key，用pop(key)    方法，对应的value也会从dict中删除：
    print(d.pop('tom'))
    print(d)
    # 和list比较，dict有以下几个特点：
    # 1、查找和插入的速度极快，不会随着key的增加而增加；
    # 2、需要占用大量的内存，内存浪费多。
    # 而list相反：
    # 1、查找和插入的时间随着元素的增加而增加；
    # 2、占用空间小，浪费内存很少。
    #     set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
    s = set([1, 2, 3])
    print(s)

    a = 'abc'
    print(a)
    # 当我们调用a.replace('a', 'A')    时，实际上调用方法replace是作用在字符串对象
    # 'abc'    上的，而这个方法虽然名字叫replace，但却没有改变字符串
    # 'abc'    的内容。相反，replace方法创建了一个新字符串
    # 'Abc'    并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串
    # 'abc'，但变量b却指向新字符串    'Abc'    了：
    print(a.replace('a', 'A'))
    print(a)
    #     定义列表和元组
    classmates = ['Michael', 'Bob', 'Tracy']
    print(classmates)
    #     获取列表个数
    print(len(classmates))
    print(classmates[0])
    print(classmates[-1])
    # 追加元素
    classmates.append('李四')
    print(classmates)
    #     元素插入到指定的位置，比如索引号为1的位置：
    classmates.insert(1, '王五')
    print(classmates)
    # 删除list末尾的元素，用pop()方法：
    print(classmates.pop())
    print(classmates)
    # 删除指定位置的元素，用pop(i)方法，其中i是索引位置：
    print(classmates.pop(1))
    print(classmates)

    # 元组：tuple和list非常类似，但是tuple一旦初始化就不能修改
    classmates = ('Michael', 'Bob', 'Tracy')
    # 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
    # list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
