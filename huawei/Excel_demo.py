# -*- coding: utf-8 -*-
import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel("D:/opt/test.xlsx")
    print(df)
    data = df.head()  # 默认读取前5行的数据
    print("获取到所有的值:\n{0}".format(data))  # 格式化输出
    print("*" * 200)

    test_data = []
    for i in df.index.values:  # 获取行号索引，并对其进行遍历
        # 根据i来获取每一行指定的数据，并利用to_dict转成字典
        row_data = df.ix[i, ["姓名", "年龄", "生日", "分数"]].to_dict()
        test_data.append(row_data)
    print("获取的数据：" + test_data)
