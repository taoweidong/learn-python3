# coding=utf-8
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
